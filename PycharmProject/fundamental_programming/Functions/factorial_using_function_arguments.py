def factorial(fact):
    s=1
    if fact>0:
        for i in range(1,fact+1):
            s=s*i
        print(s)
    elif fact==0:
        print("factorial is 1")
    else:
        print('-ve numbers')
factorial(5)