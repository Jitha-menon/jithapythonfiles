import re
x='a+'
r='aaa abc dsd avf aaa avg'
matcher=re.finditer(x,r)
for match in matcher:
 print(match.start())
 print(match.group())