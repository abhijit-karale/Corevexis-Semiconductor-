FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir fastapi uvicorn[standard] python-multipart docker
WORKDIR /app
COPY app.py /app/app.py
RUN mkdir -p /data/jobs
ENV JOB_DATA=/data/jobs
EXPOSE 8000
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
