/* 
 * Corevexis Semiconductor 
 * Example 1: LOGIC TYPES 
 */

class logic_types_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass