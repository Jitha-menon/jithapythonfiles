l=[1,2,3,4,5,6,7,8,9,12,65,87,94,40,37,84,95,80]
def bsearch():
    l.sort()
    print(l)
    ele=int(input('enter the number to search'))
    fla=0
    low=0
    high=len(l)-1
    while low<=high:
        mid=low+high//2
        if ele>l[mid]:
            low=mid+1
        elif ele<l[mid]:
            high=mid-1
        elif ele==l[mid]:
            #print(mid)
            fla=1
            break
    if fla==1:
            print("found")
    else:
            print('not found')
bsearch()

