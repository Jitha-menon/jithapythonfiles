class Mother:
    def printa(self):
        print('jitha is mother')
class Child(Mother):
    def setval(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)

class Father(Child):
    def printc(self,name,age):
        self.name=name
        self.age=age
        print(self.name, self.age)
a=Mother()
a.printa()

b=Child()
b.setval('aryan',1)
b.printa()

c=Father()
c.printc('krishna',29)
c.setval('aryan',1)
c.printa()





