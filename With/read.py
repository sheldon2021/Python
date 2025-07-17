f= open("myfile.txt")


print(f.read())

f.close()

# the same can be written using with statement like this;

with open ("file.txt") as f:
    print(f.read())


# you dont have to explicity close the file