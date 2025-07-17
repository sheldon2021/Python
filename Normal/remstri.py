def clean():

    L=[]


    n=input("enter the words into the list")
    L.extend(n.strip().split())
    print(L)


    target = input("enter the target word to be removed from the list")

    # for i in range(len(L)):
        # if target == L[i]:
        #     L.remove(target)
    while target in L:        
    # use this if u want to remove the target word until its not existing in list aka repeated words
                                # for will remove just the first occurence of word
        L.remove(target)     
    # you will get list index out of range error if u do for loop so better to use while loop
    return L

new = clean()    



print("the target has been removed", new)