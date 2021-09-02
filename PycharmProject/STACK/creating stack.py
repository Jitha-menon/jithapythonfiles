stk=[]
size=int(input('enter the size of stack'))
top=0
n=0
def push():
    global top,size
    if top>size:
        print('stack is full')
    else:
        p=int(input('enter the element to push'))
        stk.append(p)
        top+=1
def pop():
    if top<size:
            print('stack is emepty')
    else:
            stk.pop()
            top-=1
def display():
    print (stk)
while(n!=1):
        print('enter the op you want to perform')
        opt=int(input('enter 1 to push 2 for pop 3 for display'))
        if(opt==1):
            push()
        elif(opt==2):
            pop()
        elif(opt==3):
            display()
        n=int(input('press 1 for exit'))



