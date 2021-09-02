# count=0
# f1=open('words','r')
# for line in f1:
#     count=count+len(line.split())
#
# print('num of words are:',count)

count={}
f=open('words','r')
for n in f:
    wr=n.split(" ")
    for word in wr:
        if word not in count:
            count.update({word:1})

        else:
            val=int(count[word])
            val=val+1
            count.update({word:val})

print (count)