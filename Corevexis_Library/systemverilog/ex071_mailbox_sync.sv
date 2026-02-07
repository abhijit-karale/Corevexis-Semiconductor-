/* 
 * Corevexis Semiconductor 
 * Example 71: MAILBOX SYNC 
 */

class mailbox_sync_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass