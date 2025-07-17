import os



def multi():
    n=int(input("enter a number"))
    os.makedirs('tables',exist_ok=True)
    if n>=2 and n<=20:
        with open(f'tables/table_{n}','w') as m:
            for i in range(1,11):
                table = f'{n}*{i} = {n*i}\n'
                m.write(table)
            

    else:
        print("give a number greater than 1 and lesser than 21")


multi()
