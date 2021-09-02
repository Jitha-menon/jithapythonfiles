class Person:
    def read(self):
        print('person is reading')
class Student(Person):
    def exam(self):
        print('student is attending exam')

obj=Person()
obj.read()

obj1=Student()
obj1.exam()
obj1.read()