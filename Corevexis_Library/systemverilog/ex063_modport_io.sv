/* 
 * Corevexis Semiconductor 
 * Example 63: MODPORT IO 
 */

class modport_io_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass