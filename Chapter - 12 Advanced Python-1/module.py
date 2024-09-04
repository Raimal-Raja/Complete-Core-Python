def myFunc():
    print("Professor")

my = myFunc()
print(__name__) #this will tell the name of file which has imported it


#if __name__="__main__":
    # if this code is directly executed by running the file its  present in
    # print("We are directly running this code")
    # myFunc()
    # print(__name__)