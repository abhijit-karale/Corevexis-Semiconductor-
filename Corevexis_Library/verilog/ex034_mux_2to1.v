/* 
 * Corevexis Semiconductor 
 * Example 34: MUX 2TO1 
 */

module mux_2to1 (
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