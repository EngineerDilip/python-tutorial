# Python Decorator: A Comprehensive Guide (A to Z)

Python provides several **inbuilt decorators** that are commonly used to modify the behavior of functions, methods, or classes. These decorators simplify some common programming patterns like property management, static/class methods, memoization, and more.

Here are the most commonly used inbuilt decorators and their usage:

### 1\. @property

The @property decorator is used to define getter methods in a class without explicitly calling them as methods. It allows you to access a method like an attribute, making the code more readable.

#### Example:

```python  
 class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

circle = Circle(5)
print(circle.radius)  # Accessing radius like an attribute
circle.radius = 10    # Using setter to update radius
print(circle.radius)

```

#### Usage:

*   **@property**: Defines a getter for an attribute.
    
*   **@.setter**: Defines a setter for the property, allowing modifications to the attribute.
    

### 2\. @staticmethod

The @staticmethod decorator is used to define a method that belongs to the class, but does not access or modify the instance (self) or class (cls). It behaves like a normal function, except it belongs to the class's namespace.

#### Example:
```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

# Call static method without creating an instance
print(MathOperations.add(3, 5))  # Output: 8

```

#### Usage:

*   Use when a method doesn't need to interact with the class or its instances.
    
*   No self or cls arguments required.
    

### 3\. @classmethod

The @classmethod decorator is used to define a method that belongs to the class, and takes the class itself (cls) as the first argument instead of the instance (self). It can modify class-level attributes and behavior.

#### Example:

```python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_person_count(cls):
        return cls.count

p1 = Person("John")
p2 = Person("Jane")
print(Person.get_person_count())  # Output: 2

```

#### Usage:

*   Use when you need access to class attributes or want to create alternative constructors.
    

### 4\. @lru\_cache

The @lru\_cache decorator (from functools module) is used for memoization. It caches the results of a function based on its inputs to optimize repeated calls with the same arguments. It uses a Least Recently Used (LRU) cache to limit memory usage.

#### Example:

```python
from functools import lru_cache

@lru_cache(maxsize=32)  # Cache up to 32 results
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # This call will be faster due to caching

```

#### Usage:

*   Useful for expensive, repetitive function calls to save time.
    
*   maxsize: Defines the maximum number of cached calls before older ones are discarded.
    

### 5\. @abstractmethod (from abc module)

The @abstractmethod decorator is used in an abstract base class (ABC) to define methods that must be implemented in any subclass. This enforces a contract for subclasses.

#### Example:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

dog = Dog()
print(dog.sound())  # Output: Bark

```

#### Usage:

*   Enforces that subclasses must implement the abstractmethod.
    
*   Can't instantiate the abstract class without implementing all abstract methods.
    

### 6\. @dataclass (from dataclasses module)

The @dataclass decorator automatically generates special methods like \_\_init\_\_, \_\_repr\_\_, \_\_eq\_\_, and others for user-defined classes, making it easier to create classes that primarily store data.

#### Example:
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(10, 20)
print(p)  # Output: Point(x=10, y=20)

```

#### Usage:

*   Automatically adds common special methods to classes, reducing boilerplate.
    
*   Ideal for classes used for storing data.
    

### 7\. @wraps (from functools module)

The @wraps decorator is used to preserve the metadata (like docstring and function name) of the original function when writing custom decorators.

#### Example:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    """This is a greeting function"""
    print(f"Hello, {name}")

greet("Alice")
print(greet.__name__)  # Output: greet (without @wraps, it would show "wrapper")
print(greet.__doc__)   # Output: This is a greeting function

```

#### Usage:

*   Use in custom decorators to keep the original function's metadata intact.
    
*   Prevents the loss of important information like the function’s name and docstring.
    

### 8\. @contextmanager (from contextlib module)

The @contextmanager decorator simplifies the creation of context managers (used with with statements) without needing to write a full class with \_\_enter\_\_ and \_\_exit\_\_ methods.

#### Example:

```python
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    try:
        yield f
    finally:
        f.close()

# Usage with 'with' statement
with open_file("test.txt", "w") as f:
    f.write("Hello, world!")

```

#### Usage:

*   Helps create simple context managers using generators.
    
*   yield separates the setup and teardown logic.
    

### Summary of Usage

*   **@property**: Simplifies getter/setter methods.
    
*   **@staticmethod**: Defines methods that don’t access class or instance data.
    
*   **@classmethod**: Allows methods to work with class-level data.
    
*   **@lru\_cache**: Caches function results for optimization.
    
*   **@abstractmethod**: Forces subclasses to implement specific methods.
    
*   **@dataclass**: Automatically generates common class methods for data storage.
    
*   **@wraps**: Preserves original function metadata in custom decorators.
    
*   **@contextmanager**: Creates easy-to-use context managers.
    

### 9\. @singleton

While Python does not provide a built-in @singleton decorator, it's commonly used in design patterns to ensure that only one instance of a class exists throughout the program. You can implement your own @singleton decorator, like this:

#### Example:
```python
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

```

#### Usage:

*   **Custom decorator to enforce a Singleton pattern**, ensuring only one instance of a class is created.
    

### 10\. @cached\_property (from functools module)

Introduced in Python 3.8, @cached\_property is used to cache the result of a property method, so it is computed only once. This decorator is useful when the value of a property is expensive to compute but doesn't change.

#### Example:

```python
from functools import cached_property

class DataLoader:
    @cached_property
    def data(self):
        print("Loading data...")
        return [1, 2, 3, 4, 5]

loader = DataLoader()
print(loader.data)  # Prints: Loading data... [1, 2, 3, 4, 5]
print(loader.data)  # Uses the cached value, doesn't print "Loading data..."

```

#### Usage:

*   Efficient for properties where the calculation is expensive and the result does not change.
    
*   The value is cached after the first access.
    

### 11\. @asyncio.coroutine (Deprecated in favor of async def)

The @asyncio.coroutine decorator was used to define a coroutine in Python 3.4+. However, from Python 3.5 onwards, **async def** has replaced it, making @asyncio.coroutine obsolete. Coroutines allow for asynchronous programming, useful in non-blocking code (e.g., network I/O).

#### Example (async def usage):

```python
import asyncio

async def greet():
    print("Hello, world!")
    await asyncio.sleep(1)
    print("Goodbye!")

# Run coroutine
asyncio.run(greet())

```
#### Usage:

*   **async def** is now the preferred way to define coroutines.
    
*   Allows you to write asynchronous functions using await for non-blocking operations.
    

### 12\. @total\_ordering (from functools module)

The @total\_ordering decorator simplifies the process of defining all comparison methods (<, <=, >, >=) for a class. You only need to define \_\_eq\_\_ and one other comparison method, and the rest are auto-generated.

#### Example:

```python
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

```

#### Usage:

*   Reduces boilerplate by automatically implementing missing comparison methods.
    
*   Requires you to define \_\_eq\_\_ and one of the ordering methods like \_\_lt\_\_.
    

### 13\. @contextlib.suppress (from contextlib module)

The @contextlib.suppress decorator is a context manager, often used with the with statement, that suppresses specified exceptions within the block of code. This is useful for scenarios where you want to handle certain exceptions quietly.

#### Example:

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    open("non_existent_file.txt")  # Won't raise an exception if file doesn't exist

```

#### Usage:

*   Useful to **suppress specific exceptions** when you want the program to proceed without throwing errors for certain situations.
    

### 14\. @classmethodproperty (Custom, not built-in)

A common need might be to create a property that works on a class level (using @classmethod), but Python doesn't provide a built-in decorator for that. You can create your own decorator for class-level properties.

#### Example:

```python
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

print(MyClass.value)  # Output: 42

```

#### Usage:

*   This is **not built-in**, but commonly used in situations where you want a property that behaves like a class method.
    

### 15\. @runtime\_checkable (from typing module)

Introduced in Python 3.8, @runtime\_checkable is used with abstract base classes (ABCs) and protocols to allow runtime checks with isinstance() and issubclass() on those protocols.

#### Example:

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class MyProtocol(Protocol):
    def method(self):
        pass

class MyClass:
    def method(self):
        print("Method implemented")

obj = MyClass()
print(isinstance(obj, MyProtocol))  # True, because it implements 'method'

```

#### Usage:

*   **Useful for runtime validation** of classes against protocols, especially when using static typing with Protocol.
    

### 16\. @dataclass.field (from dataclasses module)

When using @dataclass, sometimes you need more control over individual fields. The dataclass.field() decorator allows you to specify options for a particular field, such as default values, default factories, or whether it should be excluded from comparison.

#### Example:

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int = field(default=0, compare=False)

p1 = Person("Alice", 30)
p2 = Person("Alice", 25)
print(p1 == p2)  # True, because 'age' is excluded from comparison

```

#### Usage:

*   Fine-tunes **behavior for individual fields** in data classes, such as excluding certain fields from comparison or adding default values.
    

### 17\. @final (from typing module)

The @final decorator (introduced in Python 3.8) is used to mark a method or class as final, meaning it cannot be overridden in subclasses.

#### Example:

```python
from typing import final

class Base:
    @final
    def method(self):
        print("This cannot be overridden")

class Derived(Base):
    def method(self):  # This will raise an error
        print("Trying to override")

```

#### Usage:

*   Prevents subclasses from **overriding a method** or a class, making it final.
    

### Summary of More Built-In Decorators:

*   **@cached\_property**: Caches property results for optimization.
    
*   **@asyncio.coroutine** (deprecated): Use async def for asynchronous coroutines.
    
*   **@total\_ordering**: Auto-generates comparison methods.
    
*   **@contextlib.suppress**: Suppresses specific exceptions in a block.
    
*   **@runtime\_checkable**: Enables runtime checks for protocols.
    
*   **@final**: Prevents methods or classes from being overridden.
    
*   **@dataclass.field**: Provides fine control over fields in data classes.
    

### 18\. @types.MethodType (from types module)

While not strictly a decorator, types.MethodType allows you to bind a function to an instance as if it were an instance method. This can be used to dynamically add methods to objects.

#### Example:
```python
from types import MethodType

class Person:
    def __init__(self, name):
        self.name = name

def greet(self):
    return f"Hello, {self.name}"

p = Person("John")
p.say_hello = MethodType(greet, p)  # Bind method to instance
print(p.say_hello())  # Output: Hello, John

```

#### Usage:

*   Dynamically **bind functions to instances** as methods.
    

### 19\. @functools.partialmethod

The @functools.partialmethod decorator is used to create a new method with some arguments pre-filled. It's a variant of functools.partial, but works specifically with methods.

#### Example:

```python
from functools import partialmethod

class MyClass:
    def greeting(self, name, message):
        print(f"{message}, {name}!")

    greet_hello = partialmethod(greeting, message="Hello")

obj = MyClass()
obj.greet_hello("Alice")  # Output: Hello, Alice!

```
#### Usage:

*   Pre-fills some arguments of a method, allowing for **reusable methods** with default values.
    

### 20\. @dataclass(eq=False, order=False) (from dataclasses module)

The dataclass decorator allows additional options to control the behavior of data classes, such as whether to include comparison (\_\_eq\_\_) or ordering (\_\_lt\_\_, \_\_gt\_\_) methods.

#### Example:

```python
from dataclasses import dataclass

@dataclass(eq=False, order=False)
class Product:
    name: str
    price: float

p1 = Product("Product1", 100.0)
p2 = Product("Product1", 100.0)
print(p1 == p2)  # False, because comparison (__eq__) is disabled

```

#### Usage:

*   **eq=False**: Disables equality comparisons (\_\_eq\_\_).
    
*   **order=False**: Disables ordering comparisons (\_\_lt\_\_, \_\_gt\_\_, etc.).
    

### 21\. @functools.update\_wrapper

The @functools.update\_wrapper decorator is similar to @wraps and is used to update a wrapper function to look more like the wrapped function by copying attributes like \_\_name\_\_, \_\_doc\_\_, etc.

#### Example:

```python
import functools

def my_decorator(func):
    @functools.update_wrapper(func)
    def wrapper(*args, **kwargs):
        print("Wrapper executed")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    """This function says hello"""
    print("Hello!")

say_hello()
print(say_hello.__name__)  # Output: say_hello
print(say_hello.__doc__)   # Output: This function says hello

```

#### Usage:

*   **Preserves metadata** of the original function when creating custom decorators.
    

### 22\. @contextlib.contextmanager

While this was mentioned earlier, the @contextmanager decorator has additional utilities beyond just managing resources like files. It's useful in **any scenario where setup and teardown steps** are needed.

#### Example (More Advanced Usage):

```python
from contextlib import contextmanager

@contextmanager
def transaction():
    print("Starting transaction")
    yield
    print("Committing transaction")

# Usage in a context
with transaction():
    print("Executing some operation")

```

#### Usage:

*   Helps implement **context managers** for operations like transactions, temporary settings, etc.
    

### 23\. @typing.overload (from typing module)

The @overload decorator is used to define multiple types for a function or method. However, it's primarily used for **static type checking** and doesn’t change runtime behavior. Each @overload defines different valid argument types for a function.

#### Example:

```python
from typing import overload

@overload
def process(value: int) -> str:
    pass

@overload
def process(value: str) -> int:
    pass

def process(value):
    if isinstance(value, int):
        return str(value)
    elif isinstance(value, str):
        return len(value)

print(process(123))  # Output: '123'
print(process("hello"))  # Output: 5

```

#### Usage:

*   Used for **type hinting** in functions that can accept multiple input types.
    

### 24\. @functools.cache\_property (newer versions)

The @functools.cache\_property is like @cached\_property but with newer optimizations in more recent Python versions (Python 3.11+). It’s meant to cache properties in a way that improves both performance and memory usage for expensive property calculations.

### 25\. @asynccontextmanager (from contextlib module)

The @asynccontextmanager decorator is used to create asynchronous context managers. These are useful when working with asynchronous code, such as handling I/O-bound resources (e.g., database connections, file reads/writes).

#### Example:

```python
from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def connect_to_db():
    print("Connecting to DB...")
    await asyncio.sleep(1)  # Simulate asynchronous I/O operation
    yield
    print("Closing DB connection...")

async def main():
    async with connect_to_db():
        print("Using the database...")

asyncio.run(main())

```

#### Usage:

*   Creates context managers that support **asynchronous operations**.
    

### 26\. @atexit.register (from atexit module)

The @atexit.register decorator registers functions to be called upon normal program termination. This is useful for cleanup tasks.

#### Example:

```python
import atexit

@atexit.register
def goodbye():
    print("Program is terminating...")

print("Program is running...")
# When the script finishes, 'goodbye()' will be called automatically

```

#### Usage:

*   Used to **register functions** that are automatically called when a program exits.
    

### 27\. @traceback.format\_exception\_only (from traceback module)

While not commonly used as a standalone decorator, this function is useful in customizing the output of exceptions in Python, primarily for debugging purposes.

### 28\. @functools.singledispatchmethod

Introduced in Python 3.8, @functools.singledispatchmethod is the method version of @singledispatch, which allows you to define generic methods that behave differently based on the type of their first argument.

#### Example:

```python
from functools import singledispatchmethod

class MathOperations:
    @singledispatchmethod
    def operate(self, value):
        raise NotImplementedError("Unsupported type")

    @operate.register
    def _(self, value: int):
        return value ** 2

    @operate.register
    def _(self, value: str):
        return value.upper()

op = MathOperations()
print(op.operate(4))  # Output: 16
print(op.operate("hello"))  # Output: HELLO

```

#### Usage:

*   **Dispatches method behavior** based on the type of the first argument.
    

### 29\. @traceback.print\_stack (from traceback module)

While not exactly a decorator, this function is useful for debugging. It can print the stack trace of the current point in the program, which is helpful when debugging code execution.

### 30\. @classmethod\_descriptor

This decorator is mainly used internally for descriptor protocol implementations in Python. It is rarely used in day-to-day programming but is involved when building more complex classes that use the descriptor protocol.

### Recap of Additional Decorators:

*   **@types.MethodType**: Binds methods dynamically to objects.
    
*   **@functools.partialmethod**: Pre-fills method arguments for easy reuse.
    
*   **@dataclass(eq=False)**: Controls comparison and ordering in data classes.
    
*   **@functools.update\_wrapper**: Preserves original function metadata.
    
*   **@typing.overload**: Defines multiple types for a function for static type checking.
    
*   **@functools.singledispatchmethod**: Allows method dispatch based on type.
    
*   **@asynccontextmanager**: Creates context managers for asynchronous operations.
    
*   **@atexit.register**: Registers functions to run at program exit.
    
*   **@functools.cache\_property**: Caches property values efficiently (newer Python).