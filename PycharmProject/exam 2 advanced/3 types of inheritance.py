class Person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age
        print('person name is:',self.name)
        print('person age is :', self.age)

class Parent(Person):
    def set(self,place,address):
        self.place=place
        self.address=address
        print(self.place,self.address)

class Child(Parent):
    def setv(self,stage):
        self.state=stage
        print(self.stage)
class Student(Child,Parent):
    def sett(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)

obj=Student()
obj.sett(78,790)
