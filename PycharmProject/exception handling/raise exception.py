a=int(input ('enter the 1st num: '))
b=int(input('enter the 2nd num: '))
if b>a:
    raise Exception('no 2 is greater')
else:
    print(a/b)