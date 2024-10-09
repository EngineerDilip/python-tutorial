"""
# Python Lambda Tutorial

This script provides a comprehensive overview of lambda function in Python. 
It demonstrates various usecases of lambda function with map(), filter()
reduce(), sorted()

## Author: Dilip Kumar
## Copyright:
Copyright (c) 2024 Dilip Kumar. All rights reserved.

#History
2024-10-10: Dilip Initial Creation 

"""
# Lambda function with arguments
add = lambda a,b: a + b
print(add(2,3)) # Output: 5


# Lambda function with no arguments
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!

# With map()

numbers = [1,2,3,4]

square = list(map(lambda x: x*x, numbers))
print(square) #Output: [1, 4, 9, 16]

# With filter to filter out

numbers = [1,2,3,4,5,6,7,8]

even = list(filter(lambda x : x % 2 == 0 ,numbers ))
print(even) #Output:[2, 4, 6, 8]

# With reduce()
from functools import reduce
numbers = [1,2,3,4,5,6,7]
total = reduce(lambda x, y: x + y, numbers)
print(total) #28

# Sorting with sorted()

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# syntax : sorted(iterable, key=None, reverse=False)
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)
# Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# More example of sorted
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # Output: ['date', 'apple', 'banana', 'cherry']

# Sorting a List of Dictionaries by a Specific Key
students = [{'name': 'John', 'grade': 90}, {'name': 'Jane', 'grade': 85}]
sorted_students = sorted(students, key=lambda student: student['grade'])
print(sorted_students)
# Output: [{'name': 'Jane', 'grade': 85}, {'name': 'John', 'grade': 90}]

# Sorting by Multiple Criteria

pairs = [(1, 2), (3, 1), (1, 1), (2, 2)]
sorted_pairs = sorted(pairs, key=lambda x: (x[0], x[1]))
print(sorted_pairs)
# Output: [(1, 1), (1, 2), (2, 2), (3, 1)]


def make_multiplier(n):
    return lambda x: x * n

threetimes = make_multiplier(3)
print(threetimes(2)) #Output: 6

