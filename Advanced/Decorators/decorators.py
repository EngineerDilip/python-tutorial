"""In Python, setters and getters are typically created using the @property decorator for getters and the @property_name.setter decorator for setters. 
These methods provide a way to access and modify instance attributes while maintaining encapsulation"""

#Example 1: setter and getter 

class Person:

    def __init__(self, age) -> None:
        self.__age = age

    @property
    def age(self):
        """getter for age"""
        return self.__age
    
    @age.setter
    def age(self,new_age):
        """setter for age"""
        if new_age < 0:
            raise ValueError("Age can not be negative")
        self.__age = new_age
    


# Usage
person = Person(25)
print(person.age)  # Calls the getter, Output: 25

person.age = 30     # Calls the setter
print(person.age)   # Output: 30

#person.age = -10  # Raises ValueError: Age cannot be negative.



#Example 2: Setter and Getter 

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive.")
        self._height = value

    @property
    def area(self):
        """Calculated property: returns the area."""
        return self._width * self._height

    @property
    def perimeter(self):
        """Calculated property: returns the perimeter."""
        return 2 * (self._width + self._height)

# Usage
rect = Rectangle(5, 10)
print(rect.area)       # Output: 50
print(rect.perimeter)  # Output: 30

rect.width = 7         # Update width
print(rect.area)       # Output: 70 (updated area based on new width)


#Example: @Classproperty

class ClassProperty:
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, obj, cls=None):
        return self.fget(cls)

class MyClass:
    _value = 42

    @ClassProperty
    def value(cls):
        return cls._value
    
    @classmethod
    def set_value(cls, new_value):
        cls._value = new_value

print(MyClass.value)  # Output: 42
MyClass.set_value(80)
print(MyClass.value) # Output:80

#Example:
"""The @lru_cache decorator in Python is used to optimize function calls by caching the results of previous function calls.
 LRU stands for "Least Recently Used," meaning that when the cache is full, the least recently used items are discarded to make room for new ones."""

from functools import lru_cache

@lru_cache(maxsize=32)  # Cache up to 32 results
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(50))  # This call will be faster due to caching
                      # 12586269025

print(fibonacci.cache_info())  # Example output: CacheInfo(hits=49, misses=51, maxsize=1000, currsize=51)
fibonacci.cache_clear()        # Clears the cache


#Example: @dataclass

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

# Instantiating the Person class
person1 = Person(name="Alice", age=30)
person2 = Person(name="Bob", age=25)

# Using the auto-generated methods
print(person1)               # Output: Person(name='Alice', age=30)
print(person1 == person2)    # Output: False
print(person1.name)          # Access attributes as usual

#Example: Key Parameters of @dataclass

"""frozen=True: Makes instances of the data class immutable."""
@dataclass(frozen=True)
class ImmutablePerson:
    name: str
    age: int

p = ImmutablePerson("Alice", 30)
# p.age = 31  # This would raise an error: FrozenInstanceError

"""order=True: Adds comparison methods based on the order of fields (like <, <=, >, and >=)."""
@dataclass(order=True)
class Student:
    name: str
    grade: int

s1 = Student("Alice", 90)
s2 = Student("Bob", 80)
print(s1 > s2)  # Output: True


"""init=False: Prevents automatic creation of __init__(); useful if custom initialization is needed."""

@dataclass(init=False)
class CustomInit:
    name: str

    def __init__(self, name):
        self.name = name.upper()

obj = CustomInit("alice")
print(obj.name)  # Output: ALICE


"""The field() function from dataclasses provides more control over individual attributes."""

from dataclasses import dataclass, field

@dataclass(order=True)
class Item:
    name: str
    quantity: int = 0
    price: float = 0.0
    tags: list = field(default_factory=list)

    def total_value(self) -> float:
        return self.quantity * self.price
    
    def add_tag(self, tag):
        self.tags.append(tag)

item1 = Item("Laptop", quantity=50, price=2.99)
item2 = Item("Phone", quantity=30, price=5.99)
item1.add_tag("Electronics")

print(item1.tags)  # Output: ['Electronics']
print(item2.tags)  # Output: []
print(item1.total_value())   # Output: 149.5
print(item1 < item2)         # Output: True (based on `order=True`)

# Example disable  (__eq__) or ordering (__lt__, __gt__) methods
from dataclasses import dataclass

@dataclass(eq=False, order=False)
class Product:
    name: str
    price: float

p1 = Product("Product1", 100.0)
p2 = Product("Product1", 100.0)
print(p1 == p2)  # False, because comparison (__eq__) is disabled


#Example: wraps function

from functools import wraps


def mydecorator(func):
    @wraps(func)
    def my_wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args,**kwargs)
        print("After function call")
        return result
    return my_wrapper


@mydecorator
def greet(name):
    """this is greet function"""
    print(f"Hello {name}")


greet("Alice")
print(greet.__name__)
print(greet.__doc__)




#Example: without context manager 

class FileManager:
    def __init__(self, path, mode):
        self.file = open(path, mode)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        self.file.close()

# Using the class-based context manager
with FileManager("example.txt", "w") as f:
    f.write("Hello, world!")
    print("Writing  completed in the file")


#Example : with contextmanager

from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    file = open(path, mode)
    try:
        yield file  # Provides the file object to the `with` block
    finally:
        file.close()  # Ensures file is closed after `with` block is exited

# Using the context manager
with open_file("example.txt", "w") as f:
    f.write("Hello, world!")



#Example: Singleton class

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class MyClass:
    def __init__(self, value):
        self.value = value

obj1 = MyClass(1)
obj2 = MyClass(2)
print(obj1 is obj2)  # True, both refer to the same instance



#Example: @cached_property

from functools import cached_property

class DataLoader:
    @cached_property
    def data(self):
        print("Loading data...")
        return [1, 2, 3, 4, 5]

loader = DataLoader()
print(loader.data)  # Prints: Loading data... [1, 2, 3, 4, 5]
print(loader.data)  # Uses the cached value, doesn't print "Loading data..."



#Example: total_ordering, need  __eq__ and atleast one(>,<,>=,<=) to auto-generate rest operators.

from functools import total_ordering

@total_ordering
class Number:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

n1 = Number(5)
n2 = Number(10)
print(n1 < n2)  # True
print(n1 <= n2) # True (auto-generated)
print(n1 > n2)  # False (auto-generated)



#Example: @runtime_checkable

from typing import Protocol, runtime_checkable

# Define a protocol with @runtime_checkable
@runtime_checkable
class Greetable(Protocol):
    def greet(self) -> str:
        ...

class Person:
    def greet(self) -> str:
        return "Hello!"

class Dog:
    def greet(self) -> str:
        return "Woof!"

# Objects of different classes can still be checked for conformity to Greetable
alice = Person()
buddy = Dog()

# Runtime check with isinstance() due to @runtime_checkable
print(isinstance(alice, Greetable))  # Output: True
print(isinstance(buddy, Greetable))  # Output: True


#Example : without @runtime_checkable

from typing import Protocol

class Walkable(Protocol):
    def walk(self) -> str:
        ...

class Animal:
    def walk(self) -> str:
        return "Walking..."

# Without @runtime_checkable, this would raise a TypeError
#print(isinstance(Animal(), Walkable))  # Raises TypeError
#TypeError: Instance and class checks can only be used with @runtime_checkable protocols



# Example: @dataclass field
# Default Values
from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    author: str = "Unknown Author"  # default value
    price: float = field(default=9.99)  # Using field to set default value

# Usage
book1 = Book(title="1984")
print(book1)  # Output: Book(title='1984', author='Unknown Author', price=9.99)

#Example:  Using default_factory

from dataclasses import dataclass, field
from typing import List

@dataclass
class Classroom:
    students: List[str] = field(default_factory=list)  # Unique list for each instance

# Usage
class1 = Classroom()
class1.students.append("Alice")
print(class1.students) # Output: ['Alice']

class2 = Classroom()
print(class2.students)  # Output: []


#Example: Excluding Fields from __init__ or __repr__

from dataclasses import dataclass, field

@dataclass
class Employee:
    name: str
    age: int
    salary: float = field(repr=False)  # Excluded from __repr__
    department: str = field(default="Engineering", init=False)  # Not in __init__

# Usage
emp = Employee(name="John", age=30, salary=50000)
print(emp)  # Output: Employee(name='John', age=30, department='Engineering')


#Example: Metadata
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float = field(default=0.0, metadata={"unit": "USD"})

# Accessing metadata
product = Product(name="Laptop")
print(product.__dataclass_fields__["price"].metadata)  # Output: {'unit': 'USD'}


#Example: MethodType to bind class method with instance

from types import MethodType

class Person:
    def __init__(self, name):
        self.name = name

def greet(self):
    return f"Hello, {self.name}"

p = Person("John")
say_hello = MethodType(greet, p)  # Bind method to instance
print(say_hello())  # Output: Hello, John


# Example: partialmethod

from functools import partialmethod

class MyClass:
    def greeting(self, name, message):
        print(f"{message}, {name}!")

    greet_hello = partialmethod(greeting, message="Hello")

obj = MyClass()
obj.greet_hello("Alice")  # Output: Hello, Alice!

