# friends ={
#     "sheldon": "",
#     "wildon": "",
#     "neha": "",
#     "snowey": ""
# }

# a = input("Enter favorite language")
# # friends.add(friends['sheldon']) cant use add method in dictonary only in sets
# friends['sheldon'] = a
# b= input ("enter favorite language")
# friends['wildon']=b

# c=input("enter favorite language")
# friends['neha'] = c

# d=input("enter favorite language")
# friends['snowey'] = d

# print("the four friends along with their fav language is ",friends)




    h = {}
    a=input("enter friends name")
    b=input("enter friends's fav language")
    h.update({a:b})

    a=input("enter friends name")
    b=input("enter friends's fav language")
    h.update({a:b})

    print(h)