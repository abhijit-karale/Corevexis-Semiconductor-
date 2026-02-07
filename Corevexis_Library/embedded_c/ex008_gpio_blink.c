/* 
 * Corevexis Semiconductor 
 * Example 8: GPIO BLINK 
 */

#include <stdint.h>

#define REG_BASE 0x40000000

void gpio_blink_init(void) {
    uint32_t *ptr = (uint32_t*)REG_BASE;
    *ptr |= (1 << 5); // Example Bit Operation
}