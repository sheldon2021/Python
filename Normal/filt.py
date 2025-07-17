n=input("enter numbers")
b = n.split()


L=[]

L.extend(b)

for item in L:
    num = int(item)
    if num%5 ==0:
        print("it is divisible by 5")
    else:
        print("it is not divisible by 5")

# def divisible5(n):
#     if n % 5 == 0:
#         return True
#     return False

# a = [1, 2, 34234, 53, 6234235, 64343, 65, 754, 45, 55]

# f = list(filter(divisible5, a))
# print(f)