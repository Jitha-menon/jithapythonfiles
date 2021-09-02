num=int(input('enter the num: '))
flag=0
if num>1:
    for i in range(2,num):
        if (num%i==0):
            flag=1
            break
if flag==0:
    print(" prime")
else:
    print('not prime')
if num%2==0:
    print('even')
else:
    print("odd")
maximum=max((i) for i in str(num))
print('max digit in given num is :',maximum)
minimum=min((i) for i in str(num))
print('min digit in given num is :',minimum)

