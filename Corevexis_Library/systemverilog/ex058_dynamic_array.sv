/* 
 * Corevexis Semiconductor 
 * Example 58: DYNAMIC ARRAY 
 */

class dynamic_array_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass