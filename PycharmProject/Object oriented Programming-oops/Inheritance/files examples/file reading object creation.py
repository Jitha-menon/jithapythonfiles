class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printv(self):
        print(self.name)
        print(self.age)

f1=open("object",'r')
for i in f1:
    l=i.split(",")
    name=l[0]
    age=l[1]
    st=Student(name,age)
    st.printv()