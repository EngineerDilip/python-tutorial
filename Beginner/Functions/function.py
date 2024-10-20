# Example 1: User define function 
def greet(name):      
    return f"Hello, {name}!"  

print(greet("Alice"))  # Output: Hello, Alice!

def add(a,b):
    return a + b

print(add(2,3)) #Output: 5


# Example 2: Inbuilts functions

print(len("Hello world"))  # Output: 11
print(sum([1,2,3]))        # Output: 6


# Example 3: Lambda function

add = lambda x,y:  x + y
print(add(4,8)) #Output: 12

# Example 4: Recursive function

def factorial(n):
    print(f"called for {n}")
    if n == 0:
        return 1
    return n * factorial(n -1)

print(factorial(5)) # Output: 120


# Example 5: Variable length arguments

def my_function(*args, **kwargs):
    print(args)  # Tuple of positional arguments
    print(kwargs) # Dictionary of keyword arguments

my_function(1,2,3,[1,2,3],"Name",age=30)

# Output :
# (1, 2, 3, [1, 2, 3], 'Name')
# {'age': 30}

# Example: map, filter and reduce function
# map
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print(squares)  # Output: [1, 4, 9, 16]

# filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

# reduce
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24


# Example : local and global keywords

x = 10      #global
def func():
    global x   # to change global var
    x = 20

func()
print(x) #Output: 20


x = 30
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)

outer()  #Output: 20
print(x) #Output: 30


# Example : Decorator function

def decorator_func(func):
    def wrapper():
        print("Before the function is called")
        func()
        print("After the function is called")
    
    return wrapper

@decorator_func
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Before the function is called
# Hello!
# After the function is called

# Example : logging method using decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def multiply(a, b):
    return a * b

print(multiply(3, 4))
# Output: Calling multiply with (3, 4) and {}
#         12


# Example: Generic function: accept any func and variable arguments

def invoke_function(func,*args,**kwargs):
    result = func(*args,**kwargs)
    print(f"function result: {result}")

def sum_func(a, b):
    return a + b

def concat_func(string, num):
    return f"{string} {num}"

def greet_func():
    return "Hello, World!"

invoke_function(sum_func,5,4)
invoke_function(concat_func,"python",3)
invoke_function(greet_func)
invoke_function(lambda a,b: a+b, 5,6)

# Output:
# function result: 9
# function result: python 3
# function result: Hello, World!
# function result: 11
