num=int(input('enter the number'))
arm=0
temp=num
while temp:
    digit=temp%10
    arm=arm+digit*digit*digit
    temp=temp//10


if num==arm:
      print('armstrong')
else:
       print('not armstrong')
