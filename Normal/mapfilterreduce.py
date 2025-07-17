from functools import reduce

# map(function, input_list)

#the function can be lambda function 

# map applies a function to all items in an input list


L = [1,2,3,4,5]

# square = lambda x : x*x
# sqlist = map(square, L)
# print(list(sqlist))

# filter -->

# def even(n):
#     if (n%2==0):
#         return True
#     return False

# onlyEven = filter(even,L) 
# # filter will show values wherever it is true
# print(list(onlyEven))


#Reduce -->

def sum(a,b):
    return a+b

mul = lambda x,y:x*y

print(reduce(sum, L))
print(reduce(mul,L))