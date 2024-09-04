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

Raimal = Employee()
# print(Raimal.name, Raimal.language)

# you can use self or anyname as a paramter in this case
Raimal.getInfo()
Employee.getInfo(Raimal)
Raimal.greet()
Raimal.goodNight()

#if you don't want pass self argument in method
# you can use static to avoid self like this: @staticmethod