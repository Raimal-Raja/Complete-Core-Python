# write a recusive function to calculate 
# the sum of first n natural numbers
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3s
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 4..... n-1 + n
sum(n) = sum(n-1) + n

'''
def sum(n):
    if(n==1): # base condition for control infitely reverse program
        return 1
    return sum(n-1) +n
n = int(input("Enter n: "))
print(sum(n))