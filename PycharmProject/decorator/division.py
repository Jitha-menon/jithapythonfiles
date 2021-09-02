def revert_val(func):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
            return func(n1,n2)
        else:
            return func(n1,n2)

    return wrapper




@revert_val
def div(num1,num2):
    return num1/num2
print(div(2,10))