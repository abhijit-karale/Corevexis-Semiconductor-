import os
import uuid
import json
import shutil
from threading import Thread
from typing import Dict, Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import docker

JOB_ROOT = os.environ.get("JOB_DATA", "/data/jobs")
os.makedirs(JOB_ROOT, exist_ok=True)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/artifacts", StaticFiles(directory=JOB_ROOT), name="artifacts")

jobs: Dict[str, Dict[str, Any]] = {}
docker_client = docker.from_env()

class FileItem(BaseModel):
    path: str
    content: str

class JobRequest(BaseModel):
    language: str
    files: list[FileItem]
    options: Dict[str, Any] | None = None

def write_files(base: str, files: list[FileItem]):
    for f in files:
        p = os.path.join(base, f.path)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(f.content)

def run_c(base: str):
    cmd = "bash -lc \"gcc -O2 -Wall -o /workspace/main /workspace/src/main.c && /workspace/main 1> /workspace/stdout.txt 2> /workspace/stderr.txt\""
    docker_client.containers.run(
        "c-runner:latest",
        command=cmd,
        remove=True,
        volumes={base: {'bind': '/workspace', 'mode': 'rw'}},
        working_dir="/workspace",
        user="0:0",
        network_disabled=True,
        mem_limit="512m",
        stderr=True,
        stdout=True,
    )

def run_verilog(base: str):
    cmd = "bash -lc \"iverilog -g2012 -o /workspace/sim.out /workspace/src/top.v /workspace/tb/tb.v && vvp /workspace/sim.out 1> /workspace/stdout.txt 2> /workspace/stderr.txt\""
    docker_client.containers.run(
        "verilog-runner:latest",
        command=cmd,
        remove=True,
        volumes={base: {'bind': '/workspace', 'mode': 'rw'}},
        working_dir="/workspace",
        user="0:0",
        network_disabled=True,
        mem_limit="512m",
        stderr=True,
        stdout=True,
    )

def write_sv_harness(base: str):
    tb = os.path.join(base, "tb", "tb.cpp")
    os.makedirs(os.path.dirname(tb), exist_ok=True)
    code = []
    code.append('#include "verilated.h"')
    code.append('#include "verilated_vcd_c.h"')
    code.append('#include "Vtop.h"')
    code.append('int main(int argc, char** argv){')
    code.append('    Verilated::commandArgs(argc, argv);')
    code.append('    Verilated::traceEverOn(true);')
    code.append('    Vtop* top = new Vtop;')
    code.append('    vluint64_t t = 0;')
    code.append('    VerilatedVcdC* tfp = new VerilatedVcdC;')
    code.append('    top->trace(tfp, 99);')
    code.append('    tfp->open("/workspace/waves.vcd");')
    code.append('    bool clk = false;')
    code.append('    bool rst = true;')
    code.append('    for (t = 0; t < 1000; t++){')
    code.append('        if (t == 50) rst = false;')
    code.append('        clk = !clk;')
    code.append('        top->clk = clk;')
    code.append('        top->rst = rst;')
    code.append('        top->eval();')
    code.append('        tfp->dump(t);')
    code.append('    }')
    code.append('    top->final();')
    code.append('    tfp->close();')
    code.append('    delete tfp;')
    code.append('    delete top;')
    code.append('    return 0;')
    code.append('}')
    with open(tb, "w", encoding="utf-8") as fh:
        fh.write("\n".join(code))

def run_systemverilog(base: str):
    write_sv_harness(base)
    cmd = "bash -lc \"verilator --sv --cc /workspace/src/top.sv --trace --exe /workspace/tb/tb.cpp && make -C obj_dir -f Vtop.mk && ./obj_dir/Vtop 1> /workspace/stdout.txt 2> /workspace/stderr.txt\""
    docker_client.containers.run(
        "sv-runner:latest",
        command=cmd,
        remove=True,
        volumes={base: {'bind': '/workspace', 'mode': 'rw'}},
        working_dir="/workspace",
        user="0:0",
        network_disabled=True,
        mem_limit="512m",
        stderr=True,
        stdout=True,
    )
def worker(job_id: str, language: str):
    base = os.path.join(JOB_ROOT, job_id)
    jobs[job_id]["status"] = "running"
    try:
        if language == "c":
            run_c(base)
        elif language == "verilog":
            run_verilog(base)
        elif language == "systemverilog":
            run_systemverilog(base)
        jobs[job_id]["status"] = "completed"
    except Exception as e:
        jobs[job_id]["status"] = "failed"
        with open(os.path.join(base, "stderr.txt"), "a", encoding="utf-8") as fh:
            fh.write("\nError: " + str(e))

@app.post("/v1/jobs")
def create_job(req: JobRequest):
    language = req.language.lower()
    if language not in {"verilog","systemverilog","c"}:
        raise HTTPException(status_code=400, detail="Unsupported language")
    job_id = uuid.uuid4().hex
    base = os.path.join(JOB_ROOT, job_id)
    os.makedirs(base, exist_ok=True)
    write_files(base, req.files)
    jobs[job_id] = {"status":"queued", "language": language}
    Thread(target=worker, args=(job_id, language), daemon=True).start()
    return {"job_id": job_id, "status": "queued"}

def artifact_url(job_id: str, name: str) -> str | None:
    p = os.path.join(JOB_ROOT, job_id, name)
    if os.path.exists(p):
        return f"/artifacts/{job_id}/{name}"
    return None

@app.get("/v1/jobs/{job_id}")
def get_job(job_id: str):
    j = jobs.get(job_id)
    if not j:
        raise HTTPException(status_code=404, detail="Not found")
    return {
        "job_id": job_id,
        "status": j["status"],
        "stdout_url": artifact_url(job_id, "stdout.txt"),
        "stderr_url": artifact_url(job_id, "stderr.txt"),
        "vcd_url": artifact_url(job_id, "waves.vcd"),
    }
