class Animal:
    def __init__(self,name):
        self.name=name

    def printv(self):
        print(self.name)


class Dog(Animal):
    def __init__(self,breed,age,name):
        super().__init__(name)
        self.breed=breed
        self.age=age

    def print(self):
        print(self.breed)
        print(self.age)

obj=Dog('doberman',3,'tuttu')
obj.printv()
obj.print()