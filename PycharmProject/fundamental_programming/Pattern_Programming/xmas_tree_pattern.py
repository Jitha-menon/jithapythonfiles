k=int(input('enter the number'))
for i in range(k):
    for j in range(k):
        print(end=" ")
    k=k-1
    for r in range(0,i+1):
        print('*',end=" ")
    print()