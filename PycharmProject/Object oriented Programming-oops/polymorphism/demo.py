#overloading

class Student:
    def show(self,num1):
        self.num1=num1
        print(self.num1)

class Person(Student):
    def show(self,num2,num3):
        self.num2=num2
        self.num3=num3
        print(num2,num3)
obj=Person()
obj.show(5,6)
obj=Person()            # not supporting in python now since it is error
obj.show(5)