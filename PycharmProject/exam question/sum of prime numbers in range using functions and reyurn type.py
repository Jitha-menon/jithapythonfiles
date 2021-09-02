def prime(min,max):
    sum=0
    for a in range(min,max):
        if a>1:
            for i in range(2,a):
                if(a%i==0):
                    
                    break
            else:
                 sum=sum+a
    return sum
print(prime(1,10))