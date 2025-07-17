# L=[]

# n=int(input("enter a number"))

# for i in range(1,11):
#     line = f"{n}*{i}= {n*i}"
#     L.append(line)

# for item in L:
#     print(item)
    

table = [str(7*i) for i in range(1,11)]
print(table)
s = "\n".join(table)
print(s)