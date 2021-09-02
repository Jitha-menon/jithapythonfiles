class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print('sum is :  ',self.a+self.b)
    def sub(self):
        print('Difference is : ',self.a-self.b)
    def mul(self):
        print('multiplication is : ',self.a*self.b)
    def div(self):
        print('Division is :',self.a/self.b)

a=int(input('enter num1: '))
b=int(input('enter num2: '))
obj=Calculator(a,b)
obj.add()
obj.sub()
obj.div()
obj.mul()

