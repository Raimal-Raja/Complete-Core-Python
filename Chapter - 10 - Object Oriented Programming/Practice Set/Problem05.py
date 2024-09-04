'''Write a class Train which has methods
to book a ticket, get status,(no of seats)
and get fare information of train running under indian Railway'''
# import random
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self,fro, to):
        print(f"ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        
    def getFare(self,fro, to):
        print(f"ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,555)}")
        
    def getStatus(self):
        print(f"The train No: {self.trainNo} has successfuly left for hyderabad")
    
    
        
t = Train(222)
t.book("Badin","Hyderabad")
t.getFare("Badin","Hyderabad")
t.getStatus()