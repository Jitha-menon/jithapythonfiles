class Parent:
    def __init__(self,age,adres):
        self.age=age
        self.adres=adres

    def printv(self):
        print(self.age)
        print(self.adres)

class Teacher(Parent):
    def __init__(self,name,salary,depart,age,adres):
        super().__init__(age,adres)
        self.name=name
        self.salary=salary
        self.depart=depart

    def print(self):
        print(self.name,self.salary,self.depart,self.age,self.adres)

    def __str__(self):
        return self.name+str(self.salary)

obj=Teacher('jitha',10000,'electronics',27,'kuzhur')
obj.print()
obj.printv()
print(obj)


