class Bank:
    bankname='SBI'
    def acccreate(self,acno):
        self.acno=acno
        self.minimal=6000
        self.balance=self.balance
    def deposit(self,amt):
        self.amt=amt
        self.balance+=amt
        print('your bank balnace is ',self.balance)
    def withdraw(self,amnt):
        self.amnt=amnt
        if amnt<=self.balance:
            print('amount withdrawed is:',self.amnt)
            self.balance-=self.amnt
        else:
            print('insufficient balance')

obj=Bank()
num=int(input('enter the accoubt number'))
obj.acccreate(num)
obj.deposit(5000)
obj.withdraw(60)

