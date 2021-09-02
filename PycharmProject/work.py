def prime(n):
    for i in range(2,n+1):
        s=0
        for j in range(2,i//2+1):
            if i%j==0:
                s=s+i
        if(s<=0):
            print(i)
prime(50)

