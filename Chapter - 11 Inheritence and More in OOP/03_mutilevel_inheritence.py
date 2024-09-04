class Employee:
    a = 22

class Programmer(Employee):
    b = 49
class Manager(Programmer):
    c = 47
    
o = Manager()
print(o.a, o.b,o.c)

