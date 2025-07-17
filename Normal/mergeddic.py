dict1 = {'a': 1, 'b':2}


dict2 = {'b':3, 'c':4}

merged = dict1 | dict2
print(merged)


# merged = dict2 | dict1 this makes dict2 priority over dict1 and b=2 will appear in merged 
