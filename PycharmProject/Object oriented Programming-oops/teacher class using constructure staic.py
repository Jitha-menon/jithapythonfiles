class Teacher:
    school='MMNSS'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def printval(self):
        print(self.name,self.salary,Teacher.school)

obj=Teacher('jitha',100000)
obj.printval()