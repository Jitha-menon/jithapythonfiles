import re
f1=open('phone','r')
x = '[+][9][1]\d{10}$'
for i in f1:
    number=i.rstrip('\n')
    matcher=re.fullmatch(x,number)
    if matcher!=None:
        print(i)


