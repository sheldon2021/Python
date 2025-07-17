def stars(n=3):
    if (n==0):
        return 
    else:
        print("*"*n)
        stars(n-1)


stars(5) 
# if 5 not specified it will take default value of n=3