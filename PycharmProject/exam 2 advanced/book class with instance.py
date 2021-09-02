class Book:
    libname='luminar'
    def __init__(self,book_name,author,pages):
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def printval(self):
        print(self.lib_name,self.book_name,self.author,self.pages,self.libname)

obj=Book('harry potter','jkrowling',900)
obj.printval()