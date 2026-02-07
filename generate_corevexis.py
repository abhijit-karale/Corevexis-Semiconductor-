import os

def create_repo():
    base_dir = "Corevexis_Library"
    categories = {
        "verilog": {
            "ext": ".v",
            "topics": [
                "basic_gates", "half_adder", "full_adder", "mux_2to1", "mux_4to1", 
                "demux_1to4", "encoder_4to2", "decoder_2to4", "comparator_4bit", "alu_8bit",
                "sr_latch", "d_ff", "jk_ff", "t_ff", "register_8bit", "shift_register_piso",
                "up_counter", "down_counter", "ring_counter", "johnson_counter", "gray_code_conv",
                "sequence_detector_1011", "vending_machine_fsm", "traffic_light_controller",
                "fifo_sync", "single_port_ram", "dual_port_ram", "rom_memory", "pwm_gen", "uart_tx"
            ]
        },
        "systemverilog": {
            "ext": ".sv",
            "topics": [
                "logic_types", "enum_states", "struct_packed", "dynamic_array", "queue_methods",
                "associative_array", "always_comb_ff", "interface_simple", "modport_io",
                "clocking_block", "class_transaction", "class_inheritance", "virtual_function",
                "rand_basic", "constraint_range", "constraint_solve_before", "mailbox_sync",
                "semaphore_key", "event_trigger", "fork_join", "fork_join_any", "fork_join_none",
                "sva_immediate", "sva_concurrent", "covergroup_bins", "cross_coverage", "virtual_interface"
            ]
        },
        "embedded_c": {
            "ext": ".c",
            "topics": [
                "bit_set_reset", "bit_toggle", "pointer_basics", "struct_padding", "volatile_usage",
                "inline_assembly", "gpio_init", "gpio_blink", "ext_interrupt", "timer_basic",
                "pwm_dimming", "adc_polling", "uart_init", "uart_send_string", "i2c_start_stop",
                "spi_transfer", "watchdog_timer", "eeprom_read_write", "lcd_16x2_driver", "rtos_task_create"
            ]
        }
    }

    for lang, info in categories.items():
        folder = os.path.join(base_dir, lang)
        os.makedirs(folder, exist_ok=True)
        
        # Create 100 files for each
        for i in range(1, 101):
            topic_idx = (i-1) % len(info['topics'])
            topic_name = info['topics'][topic_idx]
            filename = f"ex{i:03d}_{topic_name}{info['ext']}"
            
            with open(os.path.join(folder, filename), "w") as f:
                f.write(f"/* \n * Corevexis Semiconductor \n * Example {i}: {topic_name.replace('_', ' ').upper()} \n */\n\n")
                
                # Insert Actual Code Snippets based on type
                if lang == "verilog":
                    f.write(f"module {topic_name} (\n    input clk,\n    input rst,\n    input [3:0] a,\n    output reg [3:0] y\n);\n\nalways @(posedge clk) begin\n    if(rst) y <= 4'b0;\n    else y <= a; \nend\n\nendmodule")
                elif lang == "systemverilog":
                    f.write(f"class {topic_name}_class;\n  rand bit [7:0] data;\n  constraint c1 {{ data > 10; }}\n\n  function void display();\n    $display(\"Data is %d\", data);\n  endfunction\nendclass")
                else:
                    f.write(f"#include <stdint.h>\n\n#define REG_BASE 0x40000000\n\nvoid {topic_name}_init(void) {{\n    uint32_t *ptr = (uint32_t*)REG_BASE;\n    *ptr |= (1 << 5); // Example Bit Operation\n}}")

    print(f"Successfully generated 300 files in {base_dir} folder!")

create_repo()