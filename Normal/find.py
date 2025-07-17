L=[]

n=input("enter elements into the list")
B = n.split(" ")
L.extend(B)



for index,item in enumerate(L):
    print(f"the third, fifth and seventh element of the list are {L[2]}, {L[4]}, {L[6]}")
    break



