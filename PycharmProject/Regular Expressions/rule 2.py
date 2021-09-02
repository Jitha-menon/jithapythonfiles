#rule 2

import re
x='[^abc]'
matcher=re.finditer(x,'abacihugjkjkgkjjfgabbab')
print(matcher)
for match in matcher:
    print('match available at:',match.start())
    print('group is :',match.group())