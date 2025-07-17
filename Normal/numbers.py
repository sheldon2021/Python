L=[]
while len(L)<8:
    num = int(input("enter a number"))
    if num in L:
        print("already exists, change number")
    else:
        L.append(num)

print(L)
# use for i in range(8) to iterate through 8 times 


# s=set()

# n=input("enter a number")
# s.add(int(n))

# you can do this using sets as well but input numbers 8 times since sets have unique elements u dont need to add condition??

# always do while len(L) < 8 if u want the total numbers in a list to be less than a certain amount