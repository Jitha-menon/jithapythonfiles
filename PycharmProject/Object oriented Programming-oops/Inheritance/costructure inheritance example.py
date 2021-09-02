class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printv(self):
        print('name',self.name)
        print('age',self.age)


class Employee(Person):
    def __init__(self,salary,desig,id,name,age):
        super().__init__(name,age)
        self.salary=salary
        self.desig=desig
        self.id=id

    def print(self):
        print(self.salary)
        print(self.desig)
        print(self.id)


obj=Employee(100000,'developer',808,'jitha',27)
obj.printv()
obj.print()