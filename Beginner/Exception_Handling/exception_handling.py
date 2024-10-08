"""
# Python Exception Handling Tutorial

This script provides a comprehensive overview of exception handling in Python. 
It demonstrates various techniques and best practices for catching, raising, 
and managing exceptions in Python applications.

## Author: Dilip Kumar
## Copyright:
Copyright (c) 2024 Dilip Kumar. All rights reserved.

#History
2024-10-09: Dilip Initial Creation 

"""

# Example 1: Basic Try-Except Block

try:
    number = int(input("Enter a number: "))
    result = 1/number
except ValueError:
    print("That's not a valid number!")    
except ZeroDivisionError :
    print("Can not divide by Zero")
else:
    print(f"result = {result}")    



# Example 2: Finally Clause
try:
    file = open('data.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Executing cleanup actions.")
    #file.close()


# Example 3: Raising Exceptions
def check_age(age):
    if age < 18:
        raise ValueError("You must be 18 or older.")
    return age

try:
    check_age(16)
except ValueError as e:
    print(f"Error:{e}")


# Example 4: Custom Exception
class CustomError(Exception):
    def __init__(self,message):
        self.message = message

def RaiseCustomError(message):
     raise CustomError(message)

try:
    RaiseCustomError("this is my custom message")   
except CustomError as e:
    print(f"Error:{e}")


# Example 5: Multiple Exceptions in One Block
try:
    value = int("abc")
except (ValueError, TypeError):
    print("A ValueError or TypeError occurred.")


# Example 6: Chained Exceptions

def example_chained_exceptions():
    try:
        raise ValueError("Initial error.")
    except ValueError as e:
        raise RuntimeError("Secondary error occurred.") from e

try:
    example_chained_exceptions()
except RuntimeError as re:
    print(re)
    print(re.__cause__)  # This will show the original exception

#Output:
#Secondary error occurred.
#Initial error.

# Example 7: Assertions
x = -5
try:
    assert x >= 0, "x must be non-negative"
except AssertionError as e:
    print(e)


# Example 8: Logging Exceptions
import logging

try:
    x = 10 / 0
except ZeroDivisionError as e:
    logging.error("An error occurred: %s", e)

#Output
# ERROR:root:An error occurred: division by zero  


# Example 9: Exception Handling in File I/O
try:
    with open('data.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("An I/O error occurred.")


# Example 10: Handling Exceptions in Loops
data = ["10", "abc", "30"]

for item in data:
    try:
        print(int(item))
    except ValueError:
        print(f"Skipping invalid value: {item}")



# Example 11: Re-raising Exceptions
def reraise_exception():
    try:
        value = int("abc")
    except ValueError:
        print("Caught an exception.")
        raise  # Re-raises the caught exception

try:
    reraise_exception()
except Exception as e:
    print(e)

#Output:
# Caught an exception.
#invalid literal for int() with base 10: 'abc'

# Example 12: Suppressing Exceptions
import contextlib

with contextlib.suppress(FileNotFoundError):
    open('non_existent_file.txt', 'r')
    content = file.read()  # This line won't be executed
    print(content)

