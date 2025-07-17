class Employee:
    company = "ITC"

    # def __init__(self,name,salary):
    #     self.name=name 
    #     self.salary = salary
    def show(self):
        print(f"the name of employee is {self.name} and salary is {self.salary}")


class Programmer(Employee):
    comapny = "ITC infotech"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")



h = Employee()
h.name = "harry"
h.salary = 120000
h.show()
c= Programmer()
c.name = "barry"
c.language = "javascript"
c.salary = 130000
c.showLanguage()
c.show()