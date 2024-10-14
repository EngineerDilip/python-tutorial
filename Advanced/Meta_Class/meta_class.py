class MyClass:
    pass

obj = MyClass()  # MyClass is an object, and its type is `type`
print(type(MyClass))  # Output: <class 'type'>
#It means Myclass is type of 'type'


class MyMeta(type):

    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)
    
class Myclass(metaclass=MyMeta):
    pass  # Output: Creating class MyClass


#Example : Metaclass to ensure that class must have method

class InterfaceMeta(type):
    def __new__(cls, name, bases, dct):
        if 'required_method' not in dct:
            raise TypeError(f"{name} must implement 'required_method'") 
            return super().__new__(cls, name, bases, dct)  
            
class MyClass(metaclass=InterfaceMeta):
    # without required_method() Myclass will throw exception    
    def required_method(self):   
        pass  # class BadClass(metaclass=InterfaceMeta):  # This will raise an error  #

#Example : Metaclass to register classes
class RegistryMeta(type):
    registry = []  # list to store the classes

     # __new__ is responsible for creating a new class.
    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        cls.registry.append(new_class) 
        return new_class  
             
class BaseClass(metaclass=RegistryMeta): 
    pass 

class SubClass1(BaseClass): 
    pass  

class SubClass2(BaseClass): 
    pass  

print(RegistryMeta.registry)  
# Output: [<class '__main__.BaseClass'>, <class '__main__.SubClass1'>, <class '__main__.SubClass2'>]


# Example : Singletone class Implementation using Metaclassess
# Singletone meta class ensure it always return single obj.

class SingletonMeta(type):
    _instances = {} # Dictionary to store instances {class:instance}

    # Overriding __call__ for the metaclass
    # override __call__ method is invoked when you attempt to create an instance of a class i.e singletonClass()
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
             # If the class doesn't already have an instance, create one
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls] # Return the singleton instance

class singletonClass(metaclass=SingletonMeta):
    pass

# Create objects and check if they are same

obj1 = singletonClass()
obj2 = singletonClass()

# Both obj1 and obj2 point to the same instance
print( obj1 is obj2 ) #True


#Example : Metaclass (AddMethodMeta) to dynamically add a method (greet) 

class AddMethodMeta(type):
    def __new__(cls, name, bases, dct):
        dct['greet'] = lambda self: f"Hello from {name}"  # Adding a new method 'greet'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass= AddMethodMeta):
    pass


# When you create an instance of MyClass, it has a greet() method, which was dynamically added by the metaclass.
my_obj = MyClass()  
# call greet() method
print(my_obj.greet()) #Hello from MyClass
