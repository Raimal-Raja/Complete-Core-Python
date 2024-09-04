'''print multiplication table of any n number
using for loop in reverse order'''

n = int(input("Enter n: "))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")