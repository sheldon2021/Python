import string

n= input("enter sentence or paragraph")


newwo = n.translate(str.maketrans('','',string.punctuation))
user = int(input("enter minimum frequency to display"))


final = newwo.strip().lower().split()
        # newwo.lower().split() here we have to lower before split because lower is for string and split returns a list then u cant do lower on a bunch of list


seen = []
found = False

for i in range(len(final)):
    occ = final.count(final[i])
    word = final[i]
    if occ>=user:
        if word not in seen:
            print(f'The occurence of the word {final[i]} is',occ)     
            seen.append(word)  
            found = True


if not found:
    print("cant find word with that many occurences")