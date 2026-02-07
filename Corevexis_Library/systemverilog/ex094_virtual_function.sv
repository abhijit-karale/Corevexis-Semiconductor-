/* 
 * Corevexis Semiconductor 
 * Example 94: VIRTUAL FUNCTION 
 */

class virtual_function_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass