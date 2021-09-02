lst=[1,2,3,4,5,6,7,8,9,88,65,43,98,9]
def linsearch(lst):
    e=int(input('enter the elemts to search'))
    flag=0
    for i in lst:
        if i==e:
            flag=1
            break
    if flag==0:
        print('not found')
    else:
        print('found')
linsearch(lst)

