from typing import Any


class Employee:
    name = "Professor"
    language = "Python"
    Salary = "-500000"
    def getInfo(Professor):
        print(f"The language is {Professor.language}")
        
    def greet(self):
        print("Good Morning")
    @staticmethod
    def goodNight():
        print("Good Night")
        
    def __init__(self, name, salary, language):
        print("this is a dunder method")
        self.name = name
        self.language = language
        self.Salary =salary
        print(f'''The language is {self.language}\nThe name is {self.name}\nThe Salary is {salary}''')

# Raimal = Employee()

Raimal = Employee("Raimal", 1200000, "Java")

# print(Raimal.name, Raimal.language)
# Raimal.name = "Raimal"

# dunder Method those methods which start with double underscore in python
# these methods are automatically callled
# when create an object of class this method is automatically called
# only __init__ method is self called method 