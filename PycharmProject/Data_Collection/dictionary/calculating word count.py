s="hi how are you"
dict={}
words=s.split(" ")
print (words)
for i in words:
    if i not in dict:
        dict.update({i:1})
    else:
        val=int(dict[i])
        val=val+1
        dict.update({i:val})
print(dict)
