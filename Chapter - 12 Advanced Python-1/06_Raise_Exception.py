a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b== 0 or a==0):
    raise ZeroDivisionError("Hey our program is not meant to devide numbers by zero")
else:
    print(f"The division of {a} and {b} is: {a/b}")
    
# try and except do not crash program whereas raise error will do 