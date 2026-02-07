/* 
 * Corevexis Semiconductor 
 * Example 14: UART SEND STRING 
 */

#include <stdint.h>

#define REG_BASE 0x40000000

void uart_send_string_init(void) {
    uint32_t *ptr = (uint32_t*)REG_BASE;
    *ptr |= (1 << 5); // Example Bit Operation
}