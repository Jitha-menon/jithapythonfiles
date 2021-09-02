import re
x='a?' #same as a* but it counts each position not as group in a*
r='aaa abc dsd avf aaa avg'
matcher=re.finditer(x,r)
for match in matcher:
 print(match.start())
 print(match.group())