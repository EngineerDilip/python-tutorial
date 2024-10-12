class Animal:
    def __init__(self):
        print("Animal constructor")
    def sound(self):
        print("This animal makes a sound.")
    def __del__(self):
        print("Animal destructor")

class Dog(Animal):  # Inheriting from Animal class
    def __init__(self):
        print("Dog constructor")
    def sound(self):
        print("The dog barks.")
    def __del__(self):
        print("Dog destructor")

class Cat(Animal):
    def __init__(self):
        print("Cat constructor")
    def __del__(self):
        print("Cat destructor")

def main():
    print("Hello, this is the main function!")
    my_dog = Dog()
    my_dog.sound() # Output: The dog barks.
    my_cat = Cat()
    my_cat.sound()


# This checks if the script is run directly or imported as a module
if __name__ == "__main__":
    main()

'''
Output:
Hello, this is the main function!
Dog constructor
The dog barks.
Cat constructor
This animal makes a sound.
Dog destructor
Cat destructor

'''


