class Employee:
    company = "ICT"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
        
class Coder:
    language = "python"
    def printLanguages(self):
        print(f"The languages for all coder is {self.language}")
        
class Programmer(Employee, Coder):
    company = "ICT Info-Tech"
    name = "Raimal"
    language = "Python"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language}")

e = Employee()
p = Programmer()

print(p.company)
p.showLanguage()
p.printLanguages() 