a=input('enter a string')
count=0
b='aeiou'
for i in a:
    if i in b:
        count+=1
    else:
        pass
print(count)