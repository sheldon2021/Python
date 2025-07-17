class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i


    def __add__(self,c2):
        return Complex(self.r + c2.r, self.i + c2.i)
