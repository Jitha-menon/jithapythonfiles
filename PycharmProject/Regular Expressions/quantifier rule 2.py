import re
x='a*'     # counts all no:of data whether a is there or not it iterates
r='aaa abc dsd avf aaa avg'
matcher=re.finditer(x,r)
for match in matcher:
 print(match.start())
 print(match.group())