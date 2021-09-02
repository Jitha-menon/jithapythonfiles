class A:
    def printa(self):
        print('inside a')
class B(A):
    def printb(self):
        print('inside b')

class C(B):
    def printc(self):
        print('inside c')

a=A()
a.printa()

b=B()
b.printb()
b.printa()

c=C()
c.printc()
c.printa()
c.printb()