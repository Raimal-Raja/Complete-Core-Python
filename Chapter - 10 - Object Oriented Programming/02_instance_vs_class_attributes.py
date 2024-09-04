class Employee:
    name = "Professor"
    language = "Python"
    Salary = "-500000"

Raimal = Employee()
Raimal.name = "Raimal" #this instance attribute
print(Raimal.name, Raimal.language)

# instance attribute take preference over class attribute during assignment & retrival