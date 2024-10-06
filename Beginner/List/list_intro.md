*List*

a list in python is a mutable (changeable), ordered  (maintain order in which elements inserted) collection of items (or element).
List can hold items of any data types
     - Integers, strings, boolean, list, tuples,set etc
     - Custome objects
     - There is no restriction to insert inside the list as long as the data type is supported in python.
     - Immutable objects like (tuple,strings) can be inserted but their individual values can not be modified directly within the list.  Example: my_list = [(1,2),'apple']  my_list[0][0] = 5 # will throw a error since tuples are immutable.
     - Allow duplicates.
     - 
Syntax: mylist = [1,2,3,'apple',True,[4,5],(6,7),{8,9,10},{'key':'value','key2':'value'}]



| **Operation**              | **Description**                                                   | **Example**                            | **Result**                           |
|----------------------------|-------------------------------------------------------------------|----------------------------------------|--------------------------------------|
| **Create a list**           | Initialize a list with elements.                                  | `my_list = [1, 2, 3]`                 | `[1, 2, 3]`                         |
| **Access by index**         | Access an element by its index.                                   | `my_list[1]`                          | `2`                                  |
| **Negative indexing**       | Access elements from the end using negative indices.              | `my_list[-1]`                         | `3`                                  |
| **Append**                  | Add an element to the end of the list.                            | `my_list.append(4)`                   | `[1, 2, 3, 4]`                      |
| **Extend**                  | Add multiple elements to the end.                                 | `my_list.extend([5, 6])`              | `[1, 2, 3, 4, 5, 6]`                |
| **Insert**                  | Insert an element at a specific index.                            | `my_list.insert(1, 10)`               | `[1, 10, 2, 3]`                     |
| **Remove**                  | Remove the first occurrence of a value.                           | `my_list.remove(10)`                  | `[1, 2, 3]`                         |
| **Pop**                     | Remove and return an element by index (default is the last one).  | `my_list.pop()`                       | `3`, list: `[1, 2]`                 |
| **Clear**                   | Remove all elements from the list.                                | `my_list.clear()`                     | `[]`                                 |
| **Index**                   | Find the index of the first occurrence of a value.                | `my_list.index(2)`                    | `1`                                  |
| **Count**                   | Count occurrences of a specific value in the list.                | `my_list.count(2)`                    | `1`                                  |
| **Sort**                    | Sort the list in ascending order (in-place).                      | `my_list.sort()`                      | `[1, 2, 3]`                         |
| **Reverse**                 | Reverse the order of the list (in-place).                         | `my_list.reverse()`                   | `[3, 2, 1]`                         |
| **Copy**                    | Create a shallow copy of the list.                                | `new_list = my_list.copy()`           | `new_list: [1, 2, 3]`               |
| **List slicing**            | Extract a subset of the list.                                     | `my_list[1:3]`                        | `[2, 3]`                            |
| **Length**                  | Get the number of elements in the list.                           | `len(my_list)`                        | `3`                                  |
| **Concatenation**           | Combine two lists.                                                | `my_list + [4, 5]`                    | `[1, 2, 3, 4, 5]`                   |
| **Multiply**                | Repeat a list a specified number of times.                        | `my_list * 2`                         | `[1, 2, 3, 1, 2, 3]`                |
| **Check membership**        | Check if an element exists in the list.                           | `2 in my_list`                        | `True`                               |
| **List comprehension**      | Create a list based on an expression or condition.                | `[x**2 for x in my_list]`             | `[1, 4, 9]`                         |
| **Delete by index**         | Delete an element at a specific index using `del`.                | `del my_list[1]`                      | `[1, 3]`                            |

