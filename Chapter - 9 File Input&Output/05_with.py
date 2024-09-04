# with statement
f = open("myfile.txt")
print(f.read())
f.close

#the same thing can be done using "with" keyword, like this:
with open("myfile.txt") as f:
    print(f.read())

#now you don't have to explicitly close the file
# it's a syntatic sugar