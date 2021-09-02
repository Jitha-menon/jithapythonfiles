#same method and same no of arguments

class Parent:
    def show(self,num1):
        self.num1=num1
        print('hiii ',self.num1)

class Child(Parent):
    def show(self,a1):
        self.a1=a1
        print('helloo',self.a1)

obj=Child()
obj.show(90)