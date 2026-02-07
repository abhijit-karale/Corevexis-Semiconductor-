/* 
 * Corevexis Semiconductor 
 * Example 35: I2C START STOP 
 */

#include <stdint.h>

#define REG_BASE 0x40000000

void i2c_start_stop_init(void) {
    uint32_t *ptr = (uint32_t*)REG_BASE;
    *ptr |= (1 << 5); // Example Bit Operation
}