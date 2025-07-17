class Animals:
    def __init__(self):
        print("animal created")

class Pets(Animals):
    def __init__(self):
        super().__init__()
        print("Pet created")


class Dog(Pets):
    def __init__(self):
        super().__init__()
        print("dog created")

    @staticmethod
    def bark():
        print("Woof Woof")


d = Dog()
d.bark()