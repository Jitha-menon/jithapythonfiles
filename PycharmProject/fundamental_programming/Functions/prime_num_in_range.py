min= int(input('enter the min range'))
max=int(input('enter the max range'))
for i in range(min,max+1):
    if (i>1):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)



