class Employee:
    def __init__(self):
        print("this is constructor of Employee")
    a = 22

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("this is constructor of Programmer")
    b = 49
class Manager(Programmer):
    c = 47
    
o = Manager()
print(o.a, o.b,o.c)

#super method use to run the constructor of super class
