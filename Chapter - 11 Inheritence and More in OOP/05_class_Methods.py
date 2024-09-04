class A:
    a = 1
    
    #to print class attribute you need add class decorator
    # to avaid the instance attribute
    @classmethod
    def show(cls):
        print(f"The is class's attribute {cls.a}")
        
e = A()
e.a = 22

e.show()