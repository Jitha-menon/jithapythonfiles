#for loop

lst1=[1,2,3,4,5,6]
for i in lst1:
    print(i)

#Adding elemets to empty set

lst1=[]
lst1.append(8)
lst1.append('hello')
lst1.append(1.3)
print(lst1)

#nesting possible

l=[1,2,[2,3,[5,6]]]
print(l)

#updation

l=[1,2,3,4]
l.append(7)
l.remove(2)
l.clear()
del l
print(l)
