with open('log.txt') as l:
    f = l.readlines()
    print(f)
   
   
    lineno = 1
    for lines in f:
        if ("python" in lines):
            print(f'python is present ,Line Number : {lineno}')
            break
        lineno+=1
    else:
        print("python is not present")