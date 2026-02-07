/* 
 * Corevexis Semiconductor 
 * Example 23: SVA IMMEDIATE 
 */

class sva_immediate_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass