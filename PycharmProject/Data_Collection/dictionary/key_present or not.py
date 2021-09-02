dict={9:8,89:98,66:99}
print (dict)
def key(x):
    if x in dict:
        print(x,'is present')
    else:
        print(x,'is not present')
x=int(input('enter the input'))
key(x)
