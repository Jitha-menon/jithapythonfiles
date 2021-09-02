l=[-67,87,68,20,-89,-45,-60,76,84,40,-76]
newlist=[]

while l:
    min=l[0]
    for i in l:
        if i<min:
            min=i
    newlist.append(min)
    l.remove(min)
print(newlist)
print(l)