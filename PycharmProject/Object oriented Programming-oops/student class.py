class Student:
    def set_value(self,name,rollnum,schoolname):
        self.name=name
        self.rollnum=rollnum
        self.schoolname=schoolname

    def print_value(self):
        print('name of student: ',self.name)
        print('rollnumber of stufdent: ', self.rollnum)
        print('schoolname of student: ', self.schoolname)
a=Student()
a.set_value('jitha',56,'mmnssems')

a.print_value()

a2=Student()
a2.set_value('jaya',57,'nssems')
a2.print_value()



