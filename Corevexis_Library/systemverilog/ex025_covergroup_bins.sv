/* 
 * Corevexis Semiconductor 
 * Example 25: COVERGROUP BINS 
 */

class covergroup_bins_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass