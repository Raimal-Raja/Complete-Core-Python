from functools import reduce
# Map  Example
l = [1,2,3,4,4,5]

square = lambda x: x*x

sqlist = map(square,l)
print(list(sqlist))

#  Filter Example
def even(n):
    if(n%2 ==0):
        return True
    return False
onlyEven = filter(even, l)
print(list(onlyEven))

# Reduced Example
def sum(a,b):
    return a+b
print(reduce(sum,l)) #you need import reduced function from functools module