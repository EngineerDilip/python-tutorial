
# Create a class and an object
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
del my_car #explicitly delete the object


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

