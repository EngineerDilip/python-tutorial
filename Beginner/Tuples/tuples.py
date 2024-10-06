# Empty tuple
empty_tuple = ()

# Tuple with one element (comma is required for a single element tuple)
single_element_tuple = (1,)

# Tuple with multiple elements
my_tuple = (1, 2, 3, "apple", True)

my_tuple = (10, 20, 30, 40, 50)

# Access the first element
print(my_tuple[0])  # Output: 10

# Access the last element (using negative indexing)
print(my_tuple[-1])  # Output: 50

# Slicing
print(my_tuple[1:4])  # Output: (20, 30, 40)

my_tuple = (1, 2, 3, 2, 4)

# Count occurrences of 2
print(my_tuple.count(2))  # Output: 2

# Find the index of 3
print(my_tuple.index(3))  # Output: 2

my_tuple = (1, 2, 3)

# This will raise an error: TypeError: 'tuple' object does not support item assignment
#my_tuple[0] = 10  


# What can be store in tuple
my_tuple = (1, "hello", 3.14, [1, 2], {"key": "value"}, (10, 20))

print(my_tuple)

my_tuple = ([1, 2, 3],)  # Tuple containing a list
my_tuple[0].append(4)    # You can modify the list inside the tuple
print(my_tuple)          # Output: ([1, 2, 3, 4],)

# Packing
my_tuple = 1, 2, 3

# Unpacking
a, b, c = my_tuple
print(a, b, c)  # Output: 1 2 3

nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple[1][1])  # Output: 3

# List comprehension
list_comp = [x**2 for x in range(5)]

# Tuple equivalent using a generator expression
tuple_gen = tuple(x**2 for x in range(5))
print(tuple_gen)  # Output: (0, 1, 4, 9, 16)

list_to_tuple = tuple([1, 2, 3])
print(list_to_tuple)

#Tuple operations

#Combined 2 tuples
combined_tuples = (1,2,3) + (4,5,6)
print(combined_tuples)  #(1, 2, 3, 4, 5, 6)

# Repeat a tuple multiple times
repeat_tuples= (1,2,3)*3
print(repeat_tuples) #(1, 2, 3, 1, 2, 3, 1, 2, 3)

#Check if an element is present in the tuple     
is_exist = 2 in repeat_tuples
print(is_exist) #True

#Get the number of elements in the tuple
print(len(repeat_tuples)) #9
#Access element by index
print((1,2,3)[1]) #2
print(repeat_tuples[2]) #3
print(repeat_tuples.count(2)) #3 times


#Tuple can be used as dictionary: key is immutable

dictionary= {(1,2):"value"}
print(dictionary[(1,2)]) #value

