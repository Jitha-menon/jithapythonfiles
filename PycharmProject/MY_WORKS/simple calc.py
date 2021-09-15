a=int (input('enter the 1st num: '))
b=int(input("enter 2nd num:"))
print('enter \n1 for addition\n 2 for subtraction\n 3 for multiplication\n 4 for diviosion ')
i=int(input('enter choice'))
if (i==1):
  print(a+b)
elif (i==2):
  print(a-b)
elif (i==3):
  print(a*b)
elif (i==4):
  print(a/b)
else:
  print('invalid')
