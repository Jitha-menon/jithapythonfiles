class Person:
    def setv(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary = salary
        print(self.name,self.age,self.salary)

class Child(Person):
    def printc(self,name,age):
        self.name=name
        self.age=age
        print(self.name, self.age)

class Parent(Person):
    def printp(self,name,adrs):
        self.name=name
        self.adrs=adrs
        print(self.name,self.adrs)

class Student(Child):
    def prints(self,name,rollno,mark):
        self.name=name
        self.rollno=rollno
        self.mark=mark
        print(self.name,self.rollno,self.mark)

c=Student()
c.prints('jitha',12,98)
c.printc('aryan',1)