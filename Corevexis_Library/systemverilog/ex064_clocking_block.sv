/* 
 * Corevexis Semiconductor 
 * Example 64: CLOCKING BLOCK 
 */

class clocking_block_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass