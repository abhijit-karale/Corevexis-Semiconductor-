/* 
 * Corevexis Semiconductor 
 * Example 99: LCD 16X2 DRIVER 
 */

#include <stdint.h>

#define REG_BASE 0x40000000

void lcd_16x2_driver_init(void) {
    uint32_t *ptr = (uint32_t*)REG_BASE;
    *ptr |= (1 << 5); // Example Bit Operation
}