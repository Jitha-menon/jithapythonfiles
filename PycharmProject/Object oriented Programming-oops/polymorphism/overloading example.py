class Parent:
    def set(self,name ,age):
        self.name=name
        self.age=age
        print(self.name,self.age)

class Child(Parent):
    def set(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
        print(self.name,self.age,self.id)

obj=Child()
obj.set('aryan',90,1)

