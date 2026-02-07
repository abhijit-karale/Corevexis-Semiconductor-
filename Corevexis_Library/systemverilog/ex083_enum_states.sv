/* 
 * Corevexis Semiconductor 
 * Example 83: ENUM STATES 
 */

class enum_states_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass