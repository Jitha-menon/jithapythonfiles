x=5
def foo():
    global x
    x=x+10
    print(x)
foo()
print ('x is',x)
