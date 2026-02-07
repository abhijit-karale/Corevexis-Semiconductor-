/* 
 * Corevexis Semiconductor 
 * Example 20: RTOS TASK CREATE 
 */

#include <stdint.h>

#define REG_BASE 0x40000000

void rtos_task_create_init(void) {
    uint32_t *ptr = (uint32_t*)REG_BASE;
    *ptr |= (1 << 5); // Example Bit Operation
}