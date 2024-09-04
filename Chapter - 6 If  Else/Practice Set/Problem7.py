# write a program to  find out whether a given post is talking about "Profesor" or not 
post = input("Enter post: ")

if("Professor".lower() in post.lower()):
    print("This post is talking about Professor.")
else:
    print("This post is not talking about Professor.")
