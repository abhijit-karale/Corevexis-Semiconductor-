/* 
 * Corevexis Semiconductor 
 * Example 62: INTERFACE SIMPLE 
 */

class interface_simple_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass