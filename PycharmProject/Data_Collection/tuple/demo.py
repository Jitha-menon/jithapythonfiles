tup=1,2,3,4,5,6,7,3,4,'hello',(1,2,3)
print(tup)
print(type(tup))

# immutable
# keeps order
# heterogenous
# support duplicate elements
# nesting possible

tup=1,2,3,4,5,6,2,'hello',3,0      #iteration
for i in tup:
    print(i)


tup=1,2,3,4,5,6,7,8,9
print(max(tup))
print(min(tup))
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[1:4])

#unpacking of tuple

tup=1,3.4,'jitha'
print(tup)
a,b,c=tup
print(a)
print(b)
print(c)