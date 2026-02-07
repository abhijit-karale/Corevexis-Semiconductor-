/* 
 * Corevexis Semiconductor 
 * Example 61: BIT SET RESET 
 */

#include <stdint.h>

#define REG_BASE 0x40000000

void bit_set_reset_init(void) {
    uint32_t *ptr = (uint32_t*)REG_BASE;
    *ptr |= (1 << 5); // Example Bit Operation
}