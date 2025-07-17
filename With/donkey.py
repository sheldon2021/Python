# with open('donk.txt','w') as d:
#     st = "Donkey, Donkey , Donkey"
#     d.write(st)


# with open('donk.txt','r') as d:
#     ne = d.read()
#     ne = ne.replace("Donkey", "#####")
#     print(ne)


# with open('donk.txt','w') as d:
#     d.write(ne)



with open('censor.txt','w') as c:
    st = ["monkey", "donkey", "cow", "buffalo"]
    for word in st:
        c.write(word + '\n')

with open('censor.txt','r') as c:
    new = c.read()
    spl = new.split()
    print(spl)
    for i in range(len(spl)):
        spl[i] = "####"

with open('censor.txt','w') as c:
    c.write('\n'.join(spl))