/* 
 * Corevexis Semiconductor 
 * Example 18: SEMAPHORE KEY 
 */

class semaphore_key_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass