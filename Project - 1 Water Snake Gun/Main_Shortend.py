''' pattern ????
    if((computer -you) ==-1 or (computer - you) == 2):
        print("you lose")
    else:
        print("You win)
'''
import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w": -1, "g":0}
reverseDic = {1:"Snake",-1:"Water", 0:"Gun"}
you = youDict[youstr]
print(f"you chose {reverseDic[you]}\nComputer chose {reverseDic[computer]}")

if(computer ==you):
    print("It's a draw")
    
else:
#     if(computer == -1 and you ==1): -2
#         print("You Win!")
#     elif(computer == -1 and you ==0): -1
#         print("You Lose!")
#     elif(computer == 1 and you == -1): 2
#         print("You Lose!")
#     elif(computer == 1 and you ==0): 1
#         print("You Win!")
#     elif(computer == 0 and you == -1): 1
#         print("You Win!")
#     elif(computer ==0 and you ==1): -1
#         print("You Lose!")
#     else:
#         print("Something went wrong")

# the below logic is written on the basis of the value of computer - you
    if((computer -you) ==-1 or (computer - you) == 2):
        print("you lose")
    else:
        print("You win")