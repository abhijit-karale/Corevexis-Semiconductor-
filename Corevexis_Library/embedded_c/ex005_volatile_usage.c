/* 
 * Corevexis Semiconductor 
 * Example 5: VOLATILE USAGE 
 */

#include <stdint.h>

#define REG_BASE 0x40000000

void volatile_usage_init(void) {
    uint32_t *ptr = (uint32_t*)REG_BASE;
    *ptr |= (1 << 5); // Example Bit Operation
}