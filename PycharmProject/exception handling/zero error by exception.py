import inspect

a=int(input ('enter the 1st num: '))
b=int(input('enter the 2nd num: '))
try:
    c=a/b
    print(c)

except Exception as e:
    print (e.args)


