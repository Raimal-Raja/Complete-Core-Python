# write a program to calculate the grade of a student
# from his marks from the followinng scheme
#90 -100=>Ex
#80-90=>B
#70-80=>c
# 50-60=>D
# <50 =>f
# marks = int(input("Enter marks: "))

# if(marks>90 or marks==100):
#     print("Excellent! you got A")
    
# elif(marks>80 or marks==90):
#     print("you got B")

# elif(marks>70 or marks==80):
#     print("You  got C ")
# elif(marks>60 or marks==70):
#     print("you got D")
# # else:
# #     print("You are failed!")

# marks = int(input("Enter your marks: "))
# if(marks<100 and marks>=90):
#     print("you have got A")
# elif(marks<90 and marks>=80):
#     print("you have got B ")
# elif(marks<80 and marks>=70):
#     print("you have got C ")
# elif(marks<70 and marks>=60):
#     print("you have got D ")
# else:
#     print("you are failed")

marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    Grade = "A+"
elif(marks<90 and marks>=80):
    Grade = "A"
elif(marks<80 and marks>=70):
    Grade = "B"
elif(marks<70 and marks>=60):
    Grade = "C"
elif(marks<60 and marks>=50):
    Grade = "D"
else:
    Grade ="F"

print("your grade is: ",Grade)