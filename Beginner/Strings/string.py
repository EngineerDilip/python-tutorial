# Single-line string
my_string = 'Hello'

# Multi-line string (using triple quotes)
multi_line_string = '''This is a
multi-line string.'''

print(my_string,'\n', multi_line_string)

my_string = "Hello, World!"

# Access the first character
print(my_string[0])  # Output: H

# Access the last character
print(my_string[-1])  # Output: !

# Slice the first 5 characters
print(my_string[:5])  # Output: Hello

# Concatenation + to join strings
my_string = "Hello" + " World"
print (my_string)

# Repetition * to repeat
my_string = 3 * "Ha"
print(my_string)  #HaHaHa

# Check if a substring exists within a string

is_exist = "Hi" in "Hi Nerds"
print(is_exist) #True

#Get the number of characters in the string	
print(len(my_string))  #6

# Access individual characters by index
print(my_string[2]) #H
print("Hello"[4]) #o

# Extract a substring by index range
my_string = "Python Programmer"
print(my_string[0:4]) #Pyth


#Methods on string

# Upper/ Lower case converstion
print("robot".upper()) #ROBOT
print("ROBERT".lower()) #robot

# Removes leading/trailing whitespace
print("Hello  ".split()) #['Hello']

# Replaces a substring with another substring
print("Hello Dilip".replace("Dilip","world")) # Hello World

# Split
print("hello,world".split(",")) #['hello', 'world']

# Joins list elements into a string
print(",".join("world"))  # w,o,r,l,d
print("+".join(['a','b','c','d'])) # a+b+c+d

# find : Returns the index of the first occurrence
print("Hello".find('o')) #4

# Checks if the string starts/ends with a given substring
print("Hello Dilip".startswith("He")) # True
print("Hello World".endswith("ld")) # True
print("Hello".count('l')) # 2




