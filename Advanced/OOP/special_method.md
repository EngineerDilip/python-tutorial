## Python Comprehensive  Special Method (Dunder Methods): A to Z

#### 1\. \_\_add\_\_, \_\_radd\_\_, \_\_iadd\_\_

*   **Purpose**: Define behavior for the + operator.
    
    *   \_\_add\_\_: For + between instances.
        
    *   \_\_radd\_\_: For right addition (useful for non-commutative addition).
        
    *   \_\_iadd\_\_: For += in-place addition.
        
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)     # Vector(4, 6)
v1 += v2
print(v1)          # Vector(4, 6)

    
```
*   **Interview Question**: Explain the difference between \_\_add\_\_, \_\_radd\_\_, and \_\_iadd\_\_. When would you use each?
    

#### 2\. \_\_call\_\_

*   **Purpose**: Makes an instance callable like a function.
    
```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
print(double(5))  # Output: 10


```
    
*   **Interview Question**: How can \_\_call\_\_ be useful for creating function-like objects? Implement a Discount class that can apply a discount to a given price when called.
    

#### 3\. \_\_contains\_\_

*   **Purpose**: Called by the in operator to check if a value is contained within an object.
    
  ```python
  class MyList:
    def __init__(self, *values):
        self.values = list(values)

    def __contains__(self, value):
        return value in self.values

my_list = MyList(1, 2, 3)
print(2 in my_list)  # Output: True

    
```
*   **Interview Question**: How would you use \_\_contains\_\_ to customize membership testing in a custom dictionary class?
    

#### 4\. \_\_del\_\_

*   **Purpose**: Called when an object is about to be destroyed (not always reliable for releasing resources).
    
  ```python
  class Resource:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} is being deleted")

res = Resource("Resource1")
del res  # Output: Resource1 is being deleted

```
*   **Interview Challenge**: Why is \_\_del\_\_ unreliable for garbage collection, and how could with statements or try-finally blocks be a safer alternative?
    

#### 5\. \_\_enter\_\_, \_\_exit\_\_

*   **Purpose**: Implement the context management protocol to work with with statements.
    
  ```python
  class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileManager("test.txt", "w") as f:
    f.write("Hello, world!")

```
*   **Interview Question**: Describe the purpose of \_\_enter\_\_ and \_\_exit\_\_ in resource management. Implement a simple Timer context manager using these methods.
    

#### 6\. \_\_eq\_\_, \_\_ne\_\_, \_\_lt\_\_, \_\_le\_\_, \_\_gt\_\_, \_\_ge\_\_

*   **Purpose**: Define comparison operators (==, !=, <, <=, >, >=).
    
  ```python
  class Product:
    def __init__(self, price):
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

prod1 = Product(10)
prod2 = Product(20)
print(prod1 == prod2)  # False
print(prod1 < prod2)   # True

```
*   **Interview Challenge**: Explain how the \_\_lt\_\_ and \_\_gt\_\_ methods interact when chaining comparisons like a < b < c. How might functools.total\_ordering simplify custom comparisons?
    

#### 7\. \_\_getitem\_\_, \_\_setitem\_\_, \_\_delitem\_\_

*   **Purpose**: Define indexing (obj\[key\]), item setting (obj\[key\] = value), and item deletion (del obj\[key\]).
    
  ```python
  class CustomList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

clist = CustomList([1, 2, 3])
clist[1] = 42
print(clist[1])  # Output: 42
del clist[1]
print(clist.data)  # Output: [1, 3]

```
*   **Interview Question**: How can \_\_getitem\_\_ be used to implement a custom sparse matrix class?
    

#### 8\. \_\_len\_\_

*   **Purpose**: Returns the length of an object when len(obj) is called.
    
  ```python
  class Sentence:
    def __init__(self, text):
        self.words = text.split()

    def __len__(self):
        return len(self.words)

sentence = Sentence("Hello world!")
print(len(sentence))  # Output: 2

  ```
    
*   **Interview Challenge**: Why might \_\_len\_\_ be a key component for enabling iteration in a custom collection?
    

#### 9\. \_\_repr\_\_, \_\_str\_\_

*   **Purpose**:
    
    *   \_\_repr\_\_: Official string representation, often useful for debugging.
        
    *   \_\_str\_\_: Informal string representation, used by print.
        
  ```python
  class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)
print(repr(person))  # Person(name='Alice', age=30)
print(str(person))   # Alice, 30 years old

```
*   **Interview Question**: Discuss the importance of \_\_repr\_\_ vs. \_\_str\_\_. Why might \_\_repr\_\_ be useful when debugging?
    

### Tricky Challenges with Dunder Methods

1.  **Overloading Operations**: Create a custom Matrix class supporting element-wise addition and multiplication using \_\_add\_\_ and \_\_mul\_\_. Handle different matrix dimensions gracefully.
    
2.  **Polymorphism with \_\_call\_\_**: Design a Logger class that can act as a logger object when instantiated (e.g., logger("Error!")) and can print messages based on a specified log level.
    
3.  **Lazy Evaluation**: Implement a Range class that simulates Python’s range object but is customizable to any iterable pattern, e.g., generating prime numbers on demand. Implement \_\_iter\_\_ and \_\_next\_\_.