class Addition:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print('sum =',num1+num2)

a=Addition()
num1=int(input('enter the 1st num'))
num2=int(input("enter the 2nd num"))
a.add(num1,num2)
# a.add(4,5)

