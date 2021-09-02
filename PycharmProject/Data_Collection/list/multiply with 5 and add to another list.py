a=[1,2,3,4,5,6,7,8,9]
b=[]
print (a)
for i in a:
    b.append(i*5)
print(b)

#list comprehension

a=[1,2,3,4]
b=[i*5 for i in a]
print (b)
