/* 
 * Corevexis Semiconductor 
 * Example 95: RAND BASIC 
 */

class rand_basic_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass