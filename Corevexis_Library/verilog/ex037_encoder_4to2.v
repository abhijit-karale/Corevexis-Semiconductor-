/* 
 * Corevexis Semiconductor 
 * Example 37: ENCODER 4TO2 
 */

module encoder_4to2 (
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