#check whether two files are identical or not
with open("This.txt") as f:
    content1 = f.read()
with open("this_copy.txt") as f:
    content2 = f.read()
if(content1 ==content2):
    print("yes these file are identicals")
else:
    print("No these files are not identicals")