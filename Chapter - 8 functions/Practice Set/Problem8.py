# write a python function to 
# print multiplication table of a given number

def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
    return i
n = int(input("Enter N:"))
print(multiply(n))