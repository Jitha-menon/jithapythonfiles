class Parent:
    def show(self,name,adrs):
        self.name=name
        self.age=adrs
        print('hiii ',self.name,self.adrs)

class Child(Parent):
    def show(self,name,age):
        self.name=name
        self.age=age
        print('helloo',self.name,self.age)

obj=Child()
obj.show('aryan',1)