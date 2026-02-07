/* 
 * Corevexis Semiconductor 
 * Example 10: TIMER BASIC 
 */

#include <stdint.h>

#define REG_BASE 0x40000000

void timer_basic_init(void) {
    uint32_t *ptr = (uint32_t*)REG_BASE;
    *ptr |= (1 << 5); // Example Bit Operation
}