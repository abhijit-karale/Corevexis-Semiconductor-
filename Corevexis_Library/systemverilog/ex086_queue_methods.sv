/* 
 * Corevexis Semiconductor 
 * Example 86: QUEUE METHODS 
 */

class queue_methods_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass