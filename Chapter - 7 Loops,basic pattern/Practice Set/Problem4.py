# prime
n = int(input("Enter a number: "))

for i in range(2,n):
    if(n%i) == 0:
        print(f"its not prime number! {i} ")
        break
else:
    print("its prime a number! ")