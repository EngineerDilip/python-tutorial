#List
a list in python is a mutable (changeable), ordered  (maintain order in which elements inserted) collection of items (or element).
List can hold items of any data types
     - Integers, strings, boolean, list, tuples,set etc
     - Custome objects
     - There is no restriction to insert inside the list as long as the data type is supported in python.
     - Immutable objects like (tuple,strings) can be inserted but their individual values can not be modified directly within the list.  Example: my_list = [(1,2),'apple']  my_list[0][0] = 5 # will throw a error since tuples are immutable.
     - Allow duplicates.
     - 
Syntax: mylist = [1,2,3,'apple',True,[4,5],(6,7),{8,9,10},{'key':'value','key2':'value'}]
