/* 
 * Corevexis Semiconductor 
 * Example 43: CONSTRAINT SOLVE BEFORE 
 */

class constraint_solve_before_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass