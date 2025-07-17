try:
    a = int(input("enter a number"))
except Exception as e:
    print(e)

# In the code you've shown, Exception is a built-in base class for all standard exceptions in Python.

a= int(input('enter a number'))

b=int(input('enter a number'))


if (b==0):
    raise ZeroDivisionError("hey dont divide by 0")
else:
    print(f'the division value is {a/b}')



# try : 
#     some code here like n=input()


# except Exception as e :
#     print(e) or print any error message

# else: 
#     run code here, this code runs only if try works successfully or if it is an invalid input or error it goes to exception block