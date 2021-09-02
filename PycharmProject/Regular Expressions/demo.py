import re
count=0
matcher=re.finditer('ab','abaabbab')
print(matcher)
for match in matcher:
    print('match available at:',match.start())
    print('group is :',match.group())
    count=count+1
print('count=',count)