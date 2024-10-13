
# Example 1 : Create a class and an object
import sys
class Car:
    pass

my_car = Car()
print("Size of empty class object:", sys.getsizeof(my_car), "bytes")
#Size of empty class object: 48 bytes
# However it depends upon the python version and system architecture.


class Car:
    #Define constructor method
    def __init__(self, make, model):
        self.make = make  #Public attribute
        self._model = model # Protected attribute
        self.__cost = "TBD"  # Private attribute
    
    #define drive method
    def drive(self):
        print(f"The {self.make} {self._model} is driving.")
    
    # define destructor method
    def __del__(self):
         print(f"Object is destroyed.")
    


# Creating an object
my_car = Car("Toyota", "Corolla")
my_car.drive()
print(f"{my_car.make} makes {my_car._model}")
#print(my_car.__cost) # AttributeError: 'Car' object has no attribute '__cost'
print(my_car._Car__cost)  # Name mangling allows access private variable
del my_car #explicitly delete the object

# Example 2: Public, Protected, Private Access

class BankAccount:
    def __init__(self, name, balance):
        self.__balance = balance  # Private attribute __variable
        self.__name = name

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        self.__get_bank_name()
        return self.__balance
    
    def __get_bank_name(self):
        print(self.__name)
    

# Accessing balance through methods, not directly
account = BankAccount("Dilip",1000)
account.deposit(500)
#Only class public method can access private variable
print(account.get_balance())  # Output: 1500
#print(account.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'
#print(account.__get_bank_name()) # AttributeError: 'BankAccount' object has no attribute '__get_bank_name'

# Example 3: @property decorator and getter/setter function

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary #protected attr

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary can't be negative")
        self._salary = value

emp = Employee("John", 5000)
print(emp._salary) # 5000
print(emp.salary)  # Getter 5000
emp.salary = 6000  # Setter
print(emp.salary)  # Getter 6000

#Example 4: Instance, Class and Static method

class MyClass:
    class_variable = "Class variable"

    def instance_method(self):
        return f"Called instance method, accessing instance and class: {self}, {self.class_variable}"

    @classmethod
    def class_method(cls):
        return f"Called class method, accessing class: {cls}, {cls.class_variable}"

    @staticmethod
    def static_method():
        return "Called static method, no access to class or instance"

# Calling methods
obj = MyClass()

# Instance method
print(obj.instance_method())      # Accessible via instance

# Class method
print(MyClass.class_method())     # Accessible via class

# Static method
print(MyClass.static_method())    # Accessible via class

#Example 5: Static Method
class MyClass:
    class_var = "class var"
    @staticmethod
    def static_method():
        print(f"This is a static method")

    @classmethod
    def class_method(cls, var):
        print(f"This is a class method, and the class is {cls} {cls.class_var}")
        cls.class_var = var

MyClass.static_method()
MyClass.class_method("new_var") # update class_var
print(MyClass.class_var) #new_var
my_class = MyClass()
my_class.class_var = "obj_var" # will not impact class var
print(MyClass.class_var) #new_var


# Example : Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f"{other} is not Point type")

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __sub__(self,other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(f"{other} is not Point type")

# Does only support +, - between Point type objs
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Output: Point(4, 6)
p4 = p2 - p1  
print(p4) #Output: Point(2,2)
#p5 = p1 + (2,3) #TypeError: (2, 3) is not Point type
p5 = p1 + Point(2,3)
print(p5) #Output: Point(3,5)








