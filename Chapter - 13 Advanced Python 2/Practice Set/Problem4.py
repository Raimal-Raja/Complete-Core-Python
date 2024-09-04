def divisible(n):
    if (n%5==0):
        return True
    return False
a = [1112, 34355,464,22,444,555,464,453,456546]
f = list(filter(divisible,a))
print(f)