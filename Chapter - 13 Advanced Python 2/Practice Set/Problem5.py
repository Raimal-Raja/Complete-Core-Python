from functools import reduce
l = [111,2,34,45,56,5,32]

def greater(a , b):
    if (a>b):
        return a
    return b
print(reduce(greater,l))