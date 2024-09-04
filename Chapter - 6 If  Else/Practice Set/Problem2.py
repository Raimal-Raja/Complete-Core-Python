# write a program to find out a student has passed or failed
# if it requires a total of 40% and at least 33% in each subject to pass.
# assume 3 subject and take marks  as an input from the user
# marks1= int(input("Enter Marks 1: "))
# marks2= int(input("Enter Marks 2: "))
# marks3= int(input("Enter Marks 3: "))

# total_Marks = 300
# obtain = marks1+marks2+marks3
# #check for total percentage
# total_percentage = obtain/total_Marks*100

# print(total_percentage)


marks1 = int(input('Enter Marks 1: '))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# check for total percentage
total_percentage = (100*(marks1+marks2+marks3))/300
if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passsed: ",total_percentage)
else:
    print("You are failed: ", total_percentage)