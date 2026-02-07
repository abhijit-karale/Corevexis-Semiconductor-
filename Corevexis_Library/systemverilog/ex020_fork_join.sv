/* 
 * Corevexis Semiconductor 
 * Example 20: FORK JOIN 
 */

class fork_join_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass