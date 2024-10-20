# Python Functions: A Comprehensive Guide (A to Z)

## 1. What is a Function?

A **function** in Python is a block of reusable code that performs a specific task. Functions help break down complex problems into simpler, manageable pieces, making the code more readable and reusable.

### Basic Syntax:
```python
def function_name(parameters):
    """docstring"""
    # Function body
    return result
```
### Example:

 ```python
 def greet(name):      
    return f"Hello, {name}!"  
 print(greet("Alice"))  # Output: Hello, Alice!
 ```

2\. Types of Functions
----------------------

### 2.1 Built-in Functions

Python has several built-in functions such as print(), len(), sum(), etc.

 ```python
   
 print(len("Hello"))  # Output: 5  
 print(sum([1, 2, 3]))  # Output: 6 
 ```

### 2.2 User-Defined Functions

You can define your own functions using the def keyword.

 ```python
 def add(a, b):      
    return a + b  
print(add(3, 5))  # Output: 8
 ```

### 2.3 Anonymous (Lambda) Functions

Lambda functions are small anonymous functions defined with the lambda keyword.

 ```python
   
 add = lambda x, y: x + y  print(add(5, 3))  # Output: 8   
 ```

### 2.4 Recursive Functions

A function that calls itself is known as a recursive function.

 ```python
   
 def factorial(n): 
    if n == 0:
        return 1
    return n * factorial(n - 1)  

print(factorial(5))  # Output: 120   
 ```

3\. Function Arguments
----------------------

### 3.1 Positional Arguments

The most common type of argument where the order matters.

 ```python
   
 def multiply(a, b):
    return a * b  

print(multiply(2, 3))  # Output: 6   
```

### 3.2 Keyword Arguments

You can specify arguments by name, regardless of their position.

 ```python
   
 def greet(first, last): 
    return f"Hello, {first} {last}"  

print(greet(last="Doe", first="John"))  
# Output: Hello, John Doe   
```

### 3.3 Default Arguments

You can provide default values for arguments in the function definition.

 ```python
   
 def greet(name="Guest"):
    return f"Hello, {name}"  

print(greet())  # Output: Hello, Guest
```

### 3.4 Variable-Length Arguments (\*args, \*\*kwargs)

*   \*args: Allows you to pass a variable number of positional arguments.
    
*   \*\*kwargs: Allows you to pass a variable number of keyword arguments.
    

 ```python

def my_function(*args, **kwargs):
    print(args)   # Tuple of positional arguments
    print(kwargs) # Dictionary of keyword arguments

my_function(1, 2, 3, name="John", age=25)
# Output: (1, 2, 3) {'name': 'John', 'age': 25}

 ```

4\. Higher-Order Functions
--------------------------

A **higher-order function** is a function that takes another function as a parameter or returns a function as its result.

### Example: map(), filter(), and reduce()

 ```python
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
 
```

5\. Scope and Lifetime of Variables
-----------------------------------

### 5.1 Local Scope

Variables defined inside a function are only accessible within that function.

 ```python
 def func():     
     x = 10    
    print(x)  
func() # print(x)  # Error: x is not defined   
```

### 5.2 Global Scope

Variables defined outside any function are accessible globally.

 ```python
 x = 5  
 def func():      
    print(x)  

func()  # Output: 5   
```

### 5.3 global Keyword

The global keyword allows you to modify a global variable inside a function.

 ```python
 x = 10

def func():
    global x
    x = 20

func()
print(x)  # Output: 20

```

### 5.4 nonlocal Keyword

The nonlocal keyword allows you to modify a variable in the nearest enclosing scope that is not global.

 ```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)

outer()  # Output: 20

```

6\. Decorators
--------------

A **decorator** is a function that wraps another function to modify or extend its behavior.

 ```python
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

```

7\. Generic Functions
---------------------

A **generic function** works with different types of arguments.

 ```python
 def add(a, b):
    return a + b  
 
 print(add(3, 4))       
 # Output: 7 (for integers)  
 # print(add("Hello", " World"))  
 # # Output: Hello World (for strings)   
 ```

8\. Best Practices (Do’s and Don’ts)
------------------------------------

### Do’s:

1.  python  def calculate\_area(radius): pass
    
2.  python  def greet(name="Guest"): return f"Hello, {name}"
    
3.  python  def my\_function(): """This function does XYZ.""" pass
    

### Don’ts:

1.  **Avoid global variables** unless absolutely necessary.
    
```python
   def append_item(item, items=[]): 
    # BAD practice items.append(item) 
        return items
```
**Fix:**

```python
def append_item(item, items=None): 
   if items is None: 
      items = [] 
      items.append(item) 
      
    return items
```    

9\. Common Interview Questions on Functions
-------------------------------------------

1.  **What is the difference between \*args and \*\*kwargs?**
    
    *   \*args is used to pass a variable number of positional arguments.
        
    *   \*\*kwargs is used to pass a variable number of keyword arguments.
        
2.  **What are lambda functions?**
    
    *   Lambda functions are anonymous functions defined using the lambda keyword.
        
3.  **What is a decorator in Python?**
    
    *   A decorator is a higher-order function that wraps another function to modify or enhance its behavior.
        
4.  **Explain the difference between global and nonlocal.**
    
    *   global allows you to modify global variables inside a function.
        
    *   nonlocal allows you to modify variables from the nearest enclosing scope that is not global.
        
5.  **What is the purpose of the \_\_name\_\_ == '\_\_main\_\_' check in Python?**
    
    *   It ensures that the code block is executed only if the script is run directly, not when imported as a module.
        

10\. Advanced Function Features
-------------------------------

### 10.1 Function Annotations

You can add type hints using function annotations.

 ```python
 def add(x: int, y: int) -> int:      
     return x + y   
```

### 10.2 Closures

A closure is a function that remembers the environment in which it was created.

 ```python
 def outer(x):
    def inner(y):
        return x + y
    return inner

add_10 = outer(10)
print(add_10(5))  # Output: 15
 
```

### 10.3 Partial Functions

Partial functions allow you to fix a certain number of arguments in a function.

 ```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
print(square(4))  # Output: 16
  
```

11\. Practical Examples
-----------------------

### 11.1 Memoization (Caching Results)

Memoization is a technique to store previously computed results to speed up future computations.

 ```python

 def memoize(f):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper

@memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120
       
```
### 11.2 Logging Function Calls
You can use a decorator to log each time a function is called.
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def multiply(a, b):
    return a * b

multiply(3, 4)
# Output: Calling multiply with (3, 4) and {}
#         12

```
### 12. Conclusion
- Functions in Python are powerful tools for code modularity, reusability, and organization.
- From basic functions to advanced concepts like decorators, closures, and higher-order functions, mastering Python functions will significantly enhance your programming skills.
- Use the tips and best practices to write clean, efficient, and maintainable code.