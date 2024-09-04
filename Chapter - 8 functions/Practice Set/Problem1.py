# write a program using functions to find greatest of three numbrs
def greatest(a, b ,c ):
    if(a>b and a>c):
        print("A is greatest")
        return a
    elif(b>a and b>c):
        print("b is greatest")
        return b
    else:
        print("C is greatest")
        return c
a = 3
b = 5
c = 4

print(greatest(a,b,c))