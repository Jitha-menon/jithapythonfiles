class Person:
    def work(self):
        print('person is working in HP')

class Employee(Person):
    def setval(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def printval(self):
        print(self.name)
        print(self.age)
        print(self.salary)


st=Employee()
st.setval('jitha',27,100000)
st.printval()
st.work()