lst=[1,3,6,4,7,9,23,65,4,7,22,98,54,55,54,2,3,2,1,3,4]
r=[]
for i in lst:
    if i not in r:
        r.append(i)
    else:
        print(i,end=" ")
