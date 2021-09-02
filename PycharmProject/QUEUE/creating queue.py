q=[]
n=0
size=int(input ('enter the size of queue'))
def enqueue():
    if len(q)==size:
        print('queue is full')
    else:
        e=int(input('enter the element to insert'))
        q.append(e)


def dequeue():
    if len(q)==0:
        print('queue is empty')
    else:
        q.pop()

def display():
    print(q)

while(n!=1):
        print ('enter 1. to add 2. delete 3. to display')
        choice=int(input())
        if(choice==1):
            enqueue()
        elif(choice==2):
            dequeue()
        elif(choice==3):
            display()



