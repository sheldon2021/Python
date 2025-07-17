def game():
    points = 0
    print("Which is the largest mammal in the world?")
    n= input("enter your answer")
    if n.strip().lower()=="blue whale":
        points +=1
        print(f"You are correct, You now have {points}  point!")
        print(points)
    else:
        print("You are Incorrect, Sorry!")
        print(points)

    print("Which is the largest country in the world?")
    n= input("enter your answer")
    if n.strip().lower() =="russia":
        points+=1
        print(f"You are Correct, You now have{points} points!")
    else:
        print("You are Incorrect, Sorry!")
        
    print("What is the capital of Japan?")
    n=input("enter your answer")
    if n.strip().lower() =="tokyo":
        points+=1
        print(f'You are Correct,You now have {points} points!')
    else:
        print("You are Incorrect, Sorry!")
    print(f"You now have a total of {points} Points!")
    return points   

score = game()

try:
    with open('Hi-score.txt','r') as H:
        high = int(H.read().strip())
except FileNotFoundError:
    high = 0


if score > high :
    print(f"Taa-Daa! New High Score {score} points!")
    with open('Hi-score.txt','w') as H:
        H.write(str(score))

else:
    print(f"Highest score in game is {high} points!")
        
