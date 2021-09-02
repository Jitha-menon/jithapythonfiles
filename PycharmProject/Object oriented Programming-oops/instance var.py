class Person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print('name',self.name)
        print('age',self.age)
e=Person()
e.setvalue('anu',34)
e.printvalue()