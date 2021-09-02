import re
x='[0-9a-zA-Z]'
matcher=re.finditer(x,'abacihugjkFGDFjkg*@  '';978t5kjjfgabbab')
print(matcher)
for match in matcher:
    print('match available at:',match.start())
    print('group is :',match.group())