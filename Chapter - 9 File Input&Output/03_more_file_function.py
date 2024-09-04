#use of lines function
f= open("file.txt")
lines = f.readlines()
print(lines, type(lines))

f.close()


#using line function
f = open("file.txt")
line1 = f.readline()
print(line1, type(line1))

f.close()

# lines is list
# line is string

f =open('file.txt')
line = f.readline()
while(line!= ""):
    print(line)
    line = f.readline()
    
f.close()

