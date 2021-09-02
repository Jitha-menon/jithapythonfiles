import re
f1=open('valid','r')
f2=open('valid_num','w')
x='[+][9][1]\d{10}$'
for num in f1:
    number=num.rstrip('\n')
    matcher=re.fullmatch(x,number)
    if matcher!=None:
        f2.write(num)