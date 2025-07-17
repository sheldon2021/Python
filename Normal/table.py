n=int(input("enter a number"))



L=[]
for i in range(1,11):
    line = f"{n}*{i} = {n*i}"
    L.append(line)
    print(L)

with open('tables.txt','w') as t:
    for item in L:
        t.write(item + '\n')