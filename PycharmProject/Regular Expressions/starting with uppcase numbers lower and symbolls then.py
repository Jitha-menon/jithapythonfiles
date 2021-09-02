import re
n=input('enter to validate')
x='^[A-Z][a-zA-Z0-9\W]+'
match=re.fullmatch(x,n)

if match is not None:
    print('valid')
else:
    print('invalid')