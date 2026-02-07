/* 
 * Corevexis Semiconductor 
 * Example 76: FORK JOIN NONE 
 */

class fork_join_none_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass