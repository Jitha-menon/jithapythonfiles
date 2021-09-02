a={1,2,3,4,5,6,7,8,9,34,45,67,22,99,88}
odd=set()
even=set()
for i in a:
    if i %2==0:
        even.add(i)
    else:
        odd.add(i)
print("even numbers are : ",even,"\nodd numbers are : ",odd)