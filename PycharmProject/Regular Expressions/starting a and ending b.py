# import re
# n=input('enter to validate')
# x='^a[a-zA-z0-9\W]*b$'
# match=re.fullmatch(x,n)
#
# if match is not None:
#     print('valid')
# else:
#     print('invalid')

i=0
while i<5:
    print(i,end=" ")
    i+=1
    if i==3:
        break
else:
    print(0)