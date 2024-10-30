from functools import wraps

def log_methods(cls):
    def log_decorator(original_method):
        @wraps(original_method)
        def new_method(*args, **kwargs):
            print(f"Calling {original_method.__name__} with args={args} kwargs={kwargs}" )
            result = original_method(*args, **kwargs)
            print(f"{original_method.__name__} returned {result}")
            return result
        return new_method
    
    for attr_name, attr_value in cls.__dict__.items():
         if callable(attr_value):
            setattr(cls,attr_name,log_decorator(attr_value))
    return cls


@log_methods
class Calculator:
    def add(self, a, b):
        return a + b
     
    def substract(self, a, b):
        return a - b


#Client using class Calculator

calc = Calculator()
calc.add(4, 5)
calc.substract(3,2)


#Output:
#Calling add with args=(<__main__.Calculator object at 0x0000013C35D73590>, 4, 5) kwargs={}
#add returned 9
#Calling substract with args=(<__main__.Calculator object at 0x0000013C35D73590>, 3, 2) kwargs={}
#substract returned 1

