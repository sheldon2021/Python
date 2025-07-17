class Employee:
    a =1

    @classmethod
    def show(cls):
        print(f'THe class attribute of a is {cls.a}')

    @property
    def name(self):
        return f'the name is {self.fname} and last name is {self.lname}'

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e= Employee()
# e.show()
# e.a=45
e.name = "Harry Khan"
print(e.fname, e.lname)

