import re
x='a$'      #checks whether grup ends with a . $ used to denote end postion
r='aaa abc dsd avf aaa avg'
matcher=re.finditer(x,r)
for match in matcher:
 print(match.start())
 print(match.group())