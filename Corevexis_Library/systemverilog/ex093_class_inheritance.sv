/* 
 * Corevexis Semiconductor 
 * Example 93: CLASS INHERITANCE 
 */

class class_inheritance_class;
  rand bit [7:0] data;
  constraint c1 { data > 10; }

  function void display();
    $display("Data is %d", data);
  endfunction
endclass