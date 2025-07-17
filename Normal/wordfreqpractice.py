import string


n = input("enter a word or sentence")

f = int(input("enter the frequency of the word required"))


new = n.lower().strip().split()

seen=[]
found = False



for i in range(len(new)):
    occ = new.count(new[i])
    word = new[i]
    if occ>=f:
        if word not in seen:
            print(f'the occurence of the word {new[i]} is {occ}')
            seen.append(word)
            found = True
if not found:
    print("cant find word with that many occurences")   
    