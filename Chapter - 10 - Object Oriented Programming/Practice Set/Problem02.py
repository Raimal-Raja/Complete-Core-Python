# write a class "calculator" capable of finding sqaure, cube and sqaure root of a number
class Calculator:
    def __init__(self, n):
        self.n = n
        
    def sqaure(self):
        print(f'the square is: {self.n*self.n} ')
        
    def cube(self):
        print(f"the cube is: {self.n *self.n*self.n}")
    
    def sqaureroot(self):
        print(f"The sqaueroot is: {self.n**1/2}")
        
cal = Calculator(4)
cal.cube()
cal.sqaure()
cal.sqaureroot()