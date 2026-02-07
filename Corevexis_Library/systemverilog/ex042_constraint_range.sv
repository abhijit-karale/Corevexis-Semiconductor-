/* 
 * Corevexis Semiconductor 
 * Example 42: CONSTRAINT RANGE 
 */

class constraint_range_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass