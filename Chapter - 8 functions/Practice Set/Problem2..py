# write a python program using function to convert Celsuius to fahrenheit.
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f) #for shorten of program
# print(f"{f_to_c(f)} degree C")
print(f"{round(c,2)} Celcius")


# round() this function takes two parameter 
# 1 value you want to round 
# 2 decimal you want to add
