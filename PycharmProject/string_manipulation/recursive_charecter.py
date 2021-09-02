a=input('enter a string')
b=''
for i in a:
    if i not in b:
        b=b+i
    else:
        print("first recursive charcht in", a,"is",i )
        break


