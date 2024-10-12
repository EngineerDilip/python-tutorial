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

