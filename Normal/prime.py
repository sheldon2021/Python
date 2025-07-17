a = int(input("enter a number"))

for i in range(2,a):
    if a%i ==0:
        print("it is not a prime")
        break
else:
    print("it is a prime number")



    # make it such that else loop is in line with for because if u do it with if , it is a prime number multiple times.. ..
    # if u make it this way itll move out of the loop if not prime then print is prime