L= [1,2,3,4,5]


# index=0
# for item in L:
#     print(f'the item number is {index} is {item} ')
#     index+=1


# This can be simplified using enumerate function 


for index,item in enumerate(L):
    print(f"The item in number at index {index} is {item}")
