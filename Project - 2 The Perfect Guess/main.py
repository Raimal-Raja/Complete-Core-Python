import random
n = random.randint(1,100)
a = int(input("Guess a number: "))
a = -1
guesses = 1
while (a != n):
    a = int(input("Guess the number: "))
    if(a >n):
        print("lower number please!")
        guesses +=1
    else:
        print("higher number please!")
        guesses +=1
print(f"Contratulations! Professor.\nYou have guessed number in {guesses} attempts:")