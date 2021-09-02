class Student:
    school='NSS EMS SCHOOL'
    def set_value(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum

    def print_value(self):
        print('name of student: ',self.name)
        print('rollnumber of stufdent: ', self.rollnum)
        print('schoolname is: ',Student.school)
a=Student()
a.set_value('jitha',56)

a.print_value()

a2=Student()
a2.set_value('jaya',45)
a2.print_value()
