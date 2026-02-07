/* 
 * Corevexis Semiconductor 
 * Example 7: ALWAYS COMB FF 
 */

class always_comb_ff_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass