import re
f2=open('python','w')

x = '[A-Z]{3}[0-9]{2}[P}[Y][0-9]{3}$'
f1=open('python','r')
for i in f1:
    number=i.rstrip('\n')
    matcher=re.fullmatch(x,number)
    if matcher!=None:
        f2.write(number)
        f2.write('\n')




