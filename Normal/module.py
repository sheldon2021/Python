def myFunc():
    print("hello world")


if __name__ == '__main__':
    print("running the program from within")
else:
    print("running the program from outside")



myFunc()
print(__name__)