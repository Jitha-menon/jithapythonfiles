def patt(n):

    for i in range(n):
        num = 1
        for j in range(1,i):
            print(num,end=' ')
            num=num+1
        print()
patt(6)
