q=[]
n=0
front=0
rear=0
size=int(input('enter the size of element'))
def insert():
    global size,front,rear,q
    if rear>=size:
        print('queue is full')
    else:
        e=int(input('enter the element'))
        q.insert(rear,e)
        rear+=1


        for i in range (front,rear):
            print (q[i])
def delete():
    global size,front,rear,q
    if rear==front:
        print('queue if empty')
    else:
        front+=1

        for i in range(front,rear):
            print(q[i])
while(n!=1):
    print('enter the choice 1.insert 2.delete')
    choice=int(input())
    if(choice==1):
        insert()
    elif(choice==2):
        delete()


