lst=[1,2,3,4,5,6,7]
index=int(input("enter th index"))
try:
    print(lst[index])
except Exception as e:
    print (e.args)
