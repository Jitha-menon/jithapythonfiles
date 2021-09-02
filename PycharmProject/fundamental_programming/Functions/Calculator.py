def sum(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
print("enter the operation of your choice")
print ('enter 1 for addition',"2 for subtraction",'3 for multiplication ','4 for division ')
choice=int (input('enter your choice'))
a= int(input('enter the 1st num'))
b=int (input('enter the 2nd number'))
if choice==1:
    print(add(a,b))
elif choice==2:
    print(sub(a,b))
elif choice==3:
    print(mul(a,b))
elif choice==4:
    print(div(a,b))
else:
    print('invalid choice')