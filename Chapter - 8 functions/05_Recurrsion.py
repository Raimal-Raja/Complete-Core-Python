# recursion is a function which called itself
# recusion is best way to code directly an aglorithms
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
n = int(input('Enter value of N: '))
print(f"the factorial of this number is: {factorial(n)}")