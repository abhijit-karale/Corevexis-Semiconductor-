/* 
 * Corevexis Semiconductor 
 * Example 46: EVENT TRIGGER 
 */

class event_trigger_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass