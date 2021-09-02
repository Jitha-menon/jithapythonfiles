import re
x='[^a-z]'
matcher=re.finditer(x,'abacihugjkjkg*@  '';978t5kjjfgabbab')
print(matcher)
for match in matcher:
    print('match available at:',match.start())
    print('group is :',match.group())