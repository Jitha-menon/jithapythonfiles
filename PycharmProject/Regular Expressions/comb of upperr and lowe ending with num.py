import re
n=(input ('enter: '))
x='[a-zA-z]+\d$'

match=re.fullmatch(x,n)

if match is not None:
    print('valid')
else:
    print('invalid')