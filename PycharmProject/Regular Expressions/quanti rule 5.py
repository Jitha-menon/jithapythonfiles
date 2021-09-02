import re
x='a{1,3}'    #considers numbers in between both min and max range. here considers a in 2,3
r='aaa abc dsd avf aaa avg'
matcher=re.finditer(x,r)
for match in matcher:
 print(match.start())
 print(match.group())