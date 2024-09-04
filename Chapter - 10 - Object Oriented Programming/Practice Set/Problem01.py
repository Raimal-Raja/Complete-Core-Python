# create a class "Programmer" for storing information of few programmers working at microsoft
class Programmer:
    company = "Microsfot"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
p = Programmer("Raimal", 1200000, 44221)
print(p.company, p.name, p.salary, p.pin)