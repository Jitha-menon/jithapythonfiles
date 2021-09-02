num1=int(input('enter the number to check'))
flag=0
if num1>1:
    for i in range(2,num1):
        if num1%2==0:
            break
else:
        flag=1

if flag==1:
        print('prime')
else:
    print('not prime')