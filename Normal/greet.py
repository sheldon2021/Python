L=['Harry','Soham','Sachin','Rahul']


for x in L:
    if x.lower().startswith('s'):
        print(f'Hello {x}')
    else:
        print("You are not a person starting with S letter")