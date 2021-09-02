class Book:
    def show(self,author):
        self.author=author
        print('author name is ',self.author)

class Student(Book):
    def show(self,name):
        self.name=name
        print('Student name is',self.name)

obj=Student()
obj.show('jitha')