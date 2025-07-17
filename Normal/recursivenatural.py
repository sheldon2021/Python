n=int(input("enter a number"))

sum =0

def rec(n):
    if (n==0):
        return 0
    else:
        return n+rec(n-1)
            
total = rec(n)
            

print("sum of n natural numbers is ", total)
