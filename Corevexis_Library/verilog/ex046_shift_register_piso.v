/* 
 * Corevexis Semiconductor 
 * Example 46: SHIFT REGISTER PISO 
 */

module shift_register_piso (
    input clk,
    input rst,
    input [3:0] a,
    output reg [3:0] y
);

always @(posedge clk) begin
    if(rst) y <= 4'b0;
    else y <= a; 
end

endmodule