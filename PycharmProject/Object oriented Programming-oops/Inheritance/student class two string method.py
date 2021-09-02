class Student:
    college='st thomas'
    def __init__(self,name,rollno,depart):
        self.name=name
        self.rollno=rollno
        self.depart=depart
    def printv(self):
        print(self.name,self.rollno,self.depart,Student.college)

    def __str__(self):
        return self.name+self.depart+str(self.rollno)


obj=Student('jitha',56,'electronics')
obj.printv()
print(obj)