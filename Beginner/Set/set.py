#Create a set
my_set = {1,2,3,4,5,5}
print(my_set) #{1, 2, 3, 4, 5}

#Empty set
empty_set = set()

# Set from a list (duplicates will be removed)
list_set = set([1, 2, 2, 3])  # Result: {1, 2, 3}

#Unordered and Unique
my_set = {1,2,3,'apple',True,5}
print(my_set) #{1, 2, 3,5, 'apple'}

#Whats not allow to insert in set
#my_set.add([4,5]) #TypeError: unhashable type: 'list'
#my_set.add({'key':'value'}) #TypeError: unhashable type: 'dict'
my_set.add((2,1))
print(my_set) #{1, 2, 3, 5, (2, 1), 'apple'}

#Unique make set from list
my_list = [1,2,2,6,3,3,4,5,6] 
print (set(my_list)) #{1, 2, 3, 4, 5, 6}

#if you want to remove duplicate from list but want order to be maintained

unique_ordered_list =list(dict.fromkeys(my_list))
print(unique_ordered_list) #[1, 2, 6, 3, 4, 5]

#checking if element in set
print(2 in my_list) #True

#common set operations

my_set = {x**2 for x in range(4)}
print(my_set) #{0, 1, 4, 9}
#my_set = {[1,2,3]} #TypeError: unhashable type: 'list'

#frozensets are immutable sets it means its hashable
my_frozen_set = frozenset([1,2,3])
print(my_frozen_set)

#Use case of frozen set in dictionary

#my_dict = {[1,2]:'value2'}
#print(my_dict) : TypeError: unhashable type: 'list
my_dict = {frozenset([1,2]): 'value1'}
print(my_dict) #{frozenset({1, 2}): 'value1'}


#Update set in place
set1 = {1,2,3}
set2 = {4,5,6}
set1.update(set2)
print(set1) #{1, 2, 3, 4, 5, 6}

#Copy operation
#Shallow copy
original_set = {1,2,3,4,(4,5)}
#using copy method
shallow_copy= original_set.copy()
#using set() constructor
shallow_copy = set(original_set)

copied_set = original_set.copy()
print(original_set)
print(copied_set)


#Lets understand shallow copy and deep copy
import copy
print(original_set)
deep_copy = copy.deepcopy(original_set)
deep_copy.add(7)
print(original_set)
print(deep_copy)