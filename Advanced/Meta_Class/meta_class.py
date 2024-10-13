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


class RegistryMeta(type):
    registry = []

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

