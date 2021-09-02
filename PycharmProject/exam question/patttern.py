a=int(input('enter the 1st num'))
b=int(input('enter the 2nd num'))
r=5
for i in range (a,b):
    if (i%2==0):
        for k in range(r,0,-1):
            for j in range(k):
                print(i,end=' ')
            print()

    else:
        for l in range(r):
            for m in range(0,l+1):
                print(i,end=' ')
            print()