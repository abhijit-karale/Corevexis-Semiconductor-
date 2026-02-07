/* 
 * Corevexis Semiconductor 
 * Example 78: SVA CONCURRENT 
 */

class sva_concurrent_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass