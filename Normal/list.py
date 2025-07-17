L=[]

L1 = int(input("Enter values here "))


L2 = int(input("Enter values here "))


L3 = int(input("Enter values here "))


L4 = int(input("Enter values here "))
L.append(L1)
L.append(L2)
L.append(L3)
L.append(L4)

total = 0

for x in L:
    total += x
    

print("the sum is ", total)