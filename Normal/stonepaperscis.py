# 0 for stone
# 1 for paper
# 2 for scissors
import random

computer = random.choice([0,1,2])
a = (input("enter your choice: Stone/ Paper / Scissors"))

if a.strip().lower()=="stone":
    target =0 
elif a.strip().lower()=="paper":
    target = 1
elif a.strip().lower()=="scissors":
    target = 2
else:
    print("Try again with a valid choice: Stone / Paper / Scissors")
    exit()

if (computer==target):
    print("its a draw, choose again")
elif(computer==0 and target == 1):
    print("You win, Congrats")
elif(computer==0 and target == 2):
    print("You lose, Sorry")
elif(computer==1 and target == 0):
    print("You Lose, Sorry")
elif(computer==1 and target ==2):
    print("You Win, Congrats")
elif(computer==2 and target ==0):
    print("You Win, Congrats")
elif(computer==2 and target==1):
    print("You Lose, Sorry")
