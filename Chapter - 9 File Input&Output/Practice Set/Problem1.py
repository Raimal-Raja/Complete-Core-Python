''' write a program to read the textt from a given 
file "poem.txt and find out whether it contains
the  word twinkle'''

f = open("poem.txt")
txt = f.read()
if("twinkle" in txt):
    print("The word twinkle is present")
else:
    print(txt)
f.close()