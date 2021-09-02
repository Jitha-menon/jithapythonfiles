import re
n=input('enter to validate')
x='[A-Z]+[a-zA-Z0-9]{3,8}[A-Z]$'
match=re.fullmatch(x,n)

if match!= None:
    print('valid')
else:
    print('invalid')