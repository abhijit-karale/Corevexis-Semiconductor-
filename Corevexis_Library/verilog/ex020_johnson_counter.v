/* 
 * Corevexis Semiconductor 
 * Example 20: JOHNSON COUNTER 
 */

module johnson_counter (
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