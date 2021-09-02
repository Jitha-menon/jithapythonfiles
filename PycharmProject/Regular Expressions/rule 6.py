import re
x='[0-9]'
matcher=re.finditer(x,'abacihugjkjkg*@  '';978t5kjjfgabbab')
print(matcher)
for match in matcher:
    print('match available at:',match.start())
    print('group is :',match.group())