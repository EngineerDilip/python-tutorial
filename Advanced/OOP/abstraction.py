'''
Abstraction : to hide internal implementation.

'''
from abc import ABC, abstractmethod

#Abstract class Shape
class Shape(ABC):
    #decorator
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__widht = width
        self.__height = height

    # Override the area method
    def area(self):
        return self.__widht * self.__height
    

# shape = Shape() #TypeError: Can't instantiate abstract class Shape without an implementation for abstract method 'area'
rect = Rectangle(10, 20)
print(rect.area()) #Output: 200
