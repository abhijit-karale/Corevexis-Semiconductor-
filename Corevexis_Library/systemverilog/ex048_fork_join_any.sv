/* 
 * Corevexis Semiconductor 
 * Example 48: FORK JOIN ANY 
 */

class fork_join_any_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass