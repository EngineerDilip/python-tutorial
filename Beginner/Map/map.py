
#Example 1: Apply a function to each item in a list

# Basic Example: Square each number in a list
numbers = [1,2,3,4,5,6]

# Using map to apply the lambda function to square the numbers
squared_numbers = map(lambda x: x**2, numbers)
print(squared_numbers)

# Convert the map object to a list to display the results
print(list(squared_numbers))

#Output: [1, 4, 9, 16, 25, 36]

#Example 2:  Using a Named Function instead of using a lambda function, we can define a regular function.

# Named function to square a number
def square(x):
    return x**2

numbers = [2,4,6,8]
# Using map to apply the square function
squared_numbers = map(square,numbers)
print(list(squared_numbers))

#Output: [4, 16, 36, 64]

#Example 3: Working with Multiple Iterables: map() can take multiple iterables.
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

result = map(lambda x, y: x+y, list1, list2)
print("result=\t",list(result))

#Output: result=	 [11, 22, 33, 44]

#Example 4: Using map() with str Operations

words= ["python","tutorial"]

result = map(str.capitalize, words)
print(list(result))

#Output: ['Python', 'Tutorial']


#Example 5: Using map() with Complex Data Structures

pairs = [(1, 2), (3, 4), (5, 6)]

result = map(lambda x: x[0] + x[1], pairs)
print(list(result))


#Example 6: Chaining map() with Other Functional Programming Functions: 
# Using filter() and reduce() with map() for advanced transformations.

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# First, filter even numbers, then square them, then find their sum
#Filtered out the even numbers.
even_numbers = filter(lambda x: x % 2 == 0, numbers)  # Filter even numbers
#Squared the filtered numbers.
squared_even_numbers = map(lambda x: x**2, even_numbers)  # Square the even numbers
#Reduced the squared numbers by summing them.
result = reduce(lambda x, y: x + y, squared_even_numbers)  # Sum the squared values

print(result) #56


#Example 7: Using map() with Custom Classes

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y


    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

# List of points
points = [Point(1, 2), Point(3, 4), Point(5, 12)]

# Using map to get the distance from the origin for each point

distance = map(lambda point:point.distance_from_origin(),points)
print(list(distance))



#Example 8:Using map() for Data Transformation in Pandas (if applicable):
#  If you're working with dataframes or series in pandas, map() can be very useful.

import pandas as pd

# Sample data
data = pd.Series([1, 2, 3, 4])
print(data)
squared_data = data.map(lambda x: x**2)
print(squared_data)

#Output:
''' 
0     1
1     4
2     9
3    16
dtype: int64

'''