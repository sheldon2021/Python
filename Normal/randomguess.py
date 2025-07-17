import random 


g = random.randint(1, 100)
guess= 0

while True:
    guess+=1
    b=int(input("guess the number please" ))
    if (b>g):
        print("Your guess was higher than actual number")
    elif (b<g):
        print(f'Your guess was lower than actual number')
    else :
        print(f"Right Guess! Your total guesses were {guess}")
        break