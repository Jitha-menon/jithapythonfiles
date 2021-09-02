class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printv(self):
        print('name',self.name)
        print('age',self.age)

class Student(Person):
    def __init__(self,rolno,mark,name,age):
        super().__init__(name,age)
        self.rolno=rolno
        self.mark=mark
    def print(self):
        print(self.rolno)
        print(self.mark)
        print(self.name)
        print(self.age)

obj=Student(34,98,'jitha',27)



obj.printv()

obj.print()

