# Add a static method in problem 2, to greet the user with hello 

class Calculator:
    def __init__(self, n):
        self.n = n
        
    def sqaure(self):
        print(f'the square is: {self.n*self.n} ')
        
    def cube(self):
        print(f"the cube is: {self.n *self.n*self.n}")
    
    def sqaureroot(self):
        print(f"The sqaueroot is: {self.n**1/2}")
    @staticmethod #static method decorator
    def hello():
        print("Hello there")
cal = Calculator(4)
cal.hello()
cal.cube()
cal.sqaure()
cal.sqaureroot()