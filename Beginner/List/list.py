#Use cases of lists
#1. Stroing a collection of data

fruits = ['Apple','Orange','Banana']

print(type(fruits)) #type of variable
print(fruits)     #print list
print(fruits[0])  #print 1st item in a list
print(fruits[-1]) # access the last element of a list
slice = fruits[0:2] # slicing of list
print(slice)
slice.extend(['Watermelon','Dates',['CactusFruit']]) #Add multiple elements at the end
slice.insert(1,'blackGrapes') #Insert elements at the given position
slice.remove('Apple')
slice.reverse()
slice.clear() # Remove all elements from the list
fruits.index('Apple') # Get the index of first occurence of an element
fruits.count('Apple') # Count occurences of an element in the list



def print_list(list_name):
    for item in list_name:
        print (item)

print_list(fruits)
#2. Dynamic data: Can add or remove elements
fruits.append('Pineapple')
fruits.append('Grapes')
fruits.remove('Apple')

print_list(fruits)

#4. Stack and Queue Operations: LIFO, FIFO
# Stack: .append() to push
#          .pop()   to pop
# Queue: .deque()

print(fruits.pop())

#5. Sorting and Searching

numbers = [2,4,1,5,3,6,8,9]
numbers.sort() #Sorts the list in place
print_list(numbers)


#6 Aggregating Data: Lists can store intermediate results, aggregate data, and perform
# operation like summing values.

total = sum(numbers)
print("total sum of list item {}".format(total))



# Advanced Use cases

#1. List comprehensions : Concise way to create list

squares = [x**2 for x in range(4)]
print(squares)

#2. Nested List: Lists within list, useful working with matrices or complecx data struct

matrix= [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[1][2])  #print 6

#Lets Unpack the list
my_list = [1,2,3]
a,b,c = my_list # a=1,b=2,c=3
print(a,b,c)

# Lets copy the list (not reference)
# Shallow copy : creates a new list but only copies reference to the original objects(it does not duplicate nested object)
original_list = [1,2,3,4,5,6]
shallow_copy = original_list.copy()  #Using copy method

shallow_copy = my_list[:]  #Using slicing technique

shallow_copy = list(my_list) #Using list method

# Deep copy: A deep copy create a new list and also recursively copies all objects within the list( useful if the list contain nested obj)

import copy
deep_copy = copy.deepcopy(original_list)


#Thanks for learing List :)

