# create a class with attribute a; 
# create an object from it and set 'a'
# directly using object a=0.
# does this change the class attribute?
class Demo:
    a = 4
    
o = Demo()
print(o.a) #Prints the class attribute becuase instance attribute is not present
o.a  = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute beacuse instance attribute is present
print(Demo.a)  #print the class attribute


# clas attribute doesnot change but a instance attribute is set