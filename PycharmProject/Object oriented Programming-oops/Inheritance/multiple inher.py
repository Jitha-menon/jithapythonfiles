class Person:
    def setv(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name,self.age,self.address)
class Parent:
    def setval(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name,self.age,self.address)

class Employee(Person,Parent):
    def printv(self,name,age,coname):
        self.name=name
        self.age=age
        self.coname=coname
        print(self.name,self.age,self.coname)

obj=Employee()
obj.setv('jitha',27,'kuzhur')
obj.setval('jaya',50,'madhurayil')
obj.printv('kili',56,'hp')

