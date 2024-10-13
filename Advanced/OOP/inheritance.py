class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working.")
    
    def check_inherit(self):
        print("default behavior")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary) # to call base class constructor
        self.department = department

    def work(self):
        print(f"{self.name} is managing the {self.department} department.")

m = Manager("Alice", 80000, "HR")
m.work()  # Output: Alice is managing the HR department.
m.check_inherit() #Output: default behavior



# Example: Mixin classes
from abc import ABC, abstractmethod
class LogMixin:
    def log(self, message):
        print(f"LOG: {message}")

class Animal:
    @abstractmethod
    def bark(self):
        pass

class Dog(Animal, LogMixin):
    def bark(self):
        self.log("Dog is barking!")

d = Dog()
d.bark()
