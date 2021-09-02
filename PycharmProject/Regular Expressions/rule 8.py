import re
x="\w"
matcher=re.finditer(x,'abacihugjkFGDFjkg*@  '';978t5kjjfgabbab')
print(matcher)
for match in matcher:
    print('match available at:',match.start())
    print('group is :',match.group())

x="\W"
matcher=re.finditer(x,'abacihugjkFGDFjkg*@  '';978t5kjjfgabbab')
print(matcher)
for match in matcher:
    print('match available at:',match.start())
    print('group is :',match.group())