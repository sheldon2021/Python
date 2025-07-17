class Employee:
    name = "Sheldon"
    language = "python"
    
    @staticmethod
    def hello():
        print("Hello World")

shel = Employee()

print(shel.name, shel.language)
