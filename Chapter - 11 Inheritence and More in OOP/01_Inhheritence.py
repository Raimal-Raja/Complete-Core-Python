class Employee:
    company = "ICT"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
        
# class Programmer:
#     company = "ICT Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#                 print(f"The name is {self.name} and he is good with {self.language}")
class Programmer(Employee):
    company = "ICT Info-Tech"
    def showLanguage(self):
        self.name = "Raimal"
        self.language = "Python"
        print(f"The name is {self.name} and he is good with {self.language}")
e = Employee()
p = Programmer()

print(p.company)
p.showLanguage()