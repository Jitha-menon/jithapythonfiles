class Employee:
    department="IT Department"
    company="WIPRO"
    def setvalue(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.id=id
        self.salary=salary
    def printvalue(self):
        print('name: ',self.name)
        print('age: ',self.age)
        print('id: ',self.id)
        print('salary: ',self.salary)
        print('department: ',Employee.department)
        print('company : ',Employee.company)

a1=Employee()
a1.setvalue('Jitha',27,680734,100000)
a1.printvalue()

a2=Employee()
a2.setvalue('Jaya',29,680736,1000006)
a2.printvalue()



