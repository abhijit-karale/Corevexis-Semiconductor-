/* 
 * Corevexis Semiconductor 
 * Example 27: VIRTUAL INTERFACE 
 */

class virtual_interface_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass