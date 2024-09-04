'''Create a class (2D Vector) and use it to create 
another class representing a 3D vector
'''
class TwoDvector:
    def __init__(self, i,j):
        self.i =i
        self.j = j
        
    def show(self):
        print(f"the two twoDvector is {self.i}i and {self.j}j")

class ThreeDVector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k =k
        
    def show(self):
        
       print(f"the two twoDvector is {self.i}i and {self.j}j and {self.k}k")
       
a = TwoDvector(1,2)
a.show()
b = ThreeDVector(1,2,3)
b.show()