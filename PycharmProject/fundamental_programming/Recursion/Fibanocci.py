def recur_fib(n):

    if n<=1:
        return n
    else:
        return recur_fib(n-1)+recur_fib(n-2)

num=int (input('enter the number'))
for i in range (num):
    print(recur_fib(i))