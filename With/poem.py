with open ("poems.txt","w") as p:
    p.write("twinkle twinkle little star")
    
found = False
with open("poems.txt") as p:
    x = p.read()
    s = x.split()
    for k in range(len(s)):
        if s[k] == "twinkle" and found==False:
            print("the word twinkle exists")
            found = True
            break
        
    if found == False:
        print("it does not exist")
 

# with open ("poems.txt","w") as p:
#     st="twinkle twinkle little star"
#     p.write(st)

# with open ("poems.txt") as p:
#     x = p.read().split()
#     if "twinkle" in x:
#         print("match found")
#     else:
#         print("no match")
