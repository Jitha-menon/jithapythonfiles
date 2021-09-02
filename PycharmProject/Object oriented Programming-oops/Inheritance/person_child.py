class Mother:
    def setval(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print('name is ',self.name)
        print ('age is : ',self.age)
        print('address is: ',self.address)

class Child:
    def setv(self,name,age):
        self.name=name
        self.age=age
        print('child name is :',self.name)
        print('child age is :', self.age)
class Father(Mother,Child):
    def printv(self,name,age):
        self.name=name
        self.age=age
        print('father name is :', self.name)
        print('father age is :', self.age)

obj=Father()
obj.setval('jitha',27,'kuzhur')
obj.setv('Aryan',1)
obj.printv('krishna',29)
