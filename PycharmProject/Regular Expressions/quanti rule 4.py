import re
x='a{2}'   #considers a in the no:of positions given.here considers a repeating 2 times
r='aaa abc dsd avf aaa avg'
matcher=re.finditer(x,r)
for match in matcher:
 print(match.start())
 print(match.group())