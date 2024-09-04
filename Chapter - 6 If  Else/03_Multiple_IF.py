a = int(input("Enter your age: "))

#if statement no:1
if (a%2==0):
    print("a is even")
# End of if statement no:1

#if statement no:2
if(a>18):
    print("You are above the age of consent!")
    print("That's great!")
elif(a>0):
    print("you are entering invalid negative age!")

elif(a==0):
    print("you are entering invalid age!")
else:
    print("you are the below the age of consent!")
# End of if statement no:2
    
print('End of Program:')