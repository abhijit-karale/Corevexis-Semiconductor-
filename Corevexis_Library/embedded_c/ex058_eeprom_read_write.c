/* 
 * Corevexis Semiconductor 
 * Example 58: EEPROM READ WRITE 
 */

#include <stdint.h>

#define REG_BASE 0x40000000

void eeprom_read_write_init(void) {
    uint32_t *ptr = (uint32_t*)REG_BASE;
    *ptr |= (1 << 5); // Example Bit Operation
}