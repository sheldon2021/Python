try:
    with open('1.txt','r') as o:
        print(o.read())
except Exception as e:
    print(e)
try:
    with open('2.txt','r') as o:
        print(o.read())
except Exception as e:
    print(e)

try:
    with open('3.txt','r') as o:
        print(o.read())
except Exception as e:
    print(e)


print("thank you!")