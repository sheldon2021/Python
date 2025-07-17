class Calculator():
    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f'the square of a number is {self.n*self.n}')

    def cube(self):
        print(f'the cube of a number is {self.n*self.n*self.n}')

    def rt(self):
        print(f'the square root of a number is {self.n*1/2}')


r = Calculator(4)
r.square()
r.cube()
r.rt()