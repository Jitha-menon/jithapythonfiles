class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark

    def print(self):
        print(self.name)
        print(self.rollno)
        print(self.course)
        print(self.mark)

lst=[]
f=open('mark','r')
for i in f:
    d=i.rstrip('\n').split(',')
    print(d)
    name=d[0]
    rollno=d[1]
    course=d[2]
    mark=d[3]
    s1=Student(name,rollno,course,mark)
    s1.print()
    lst.append(s1)

mark=[]
for st in lst:
    mark.append(st.mark)
    print(mark)
for st in lst:
    if (st.mark==max(mark)):
        print(st.name,st.rollno,st.course,st.mark)