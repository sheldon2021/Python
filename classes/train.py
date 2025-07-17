
from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"ticket is booked in train No : {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f'Train is successfully running')

    def getFare(self,fro, to):
        print(f'Train prices from {fro} to {to} are {randint(100,500)}rupees on {self.trainNo}')



h = Train(45682)
h.book("Mangalore", "Bangalore")
h.getStatus()
h.getFare("Mangalore","Bangalore")