def twoSum():
    num = input("enter numbers sepearted by space")
    num2 = num.split(" ")
    lis = []
    for i in num2:
        num3 = int(i)
        lis.append(num3)
    target = int(input("enter target integer"))
    for x in range(len(lis)):
        for y in range(x+1, len(lis)):
          if lis[x]+lis[y] ==target:
            print("indices are ", x,y)
            return
    print("no pair found")


twoSum()

