from functools import reduce

l = [11, 2, 65, 53, 635, 65, 74, 45, 55]

def greater(a, b):
    if a > b:
        return a
    return b

print(reduce(greater, l))