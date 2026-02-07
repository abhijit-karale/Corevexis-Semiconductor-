/* 
 * Corevexis Semiconductor 
 * Example 26: CROSS COVERAGE 
 */

class cross_coverage_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass