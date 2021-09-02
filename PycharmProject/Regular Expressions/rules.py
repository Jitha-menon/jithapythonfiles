# x='[abc]'
# x='[^abc]'
# x='[a-z]'
# x='[a-zA-z]'
# x='[0-9]'
# x='[^a-zA0-9]'
# x='\s'
# x='\d'
# x='\D'
# x='\w'
# x='\W

# rule 1 example

import re
x='[abc]'
matcher=re.finditer(x,'abacihugjkjkgkjjfgabbab')
print(matcher)
for match in matcher:
    print('match available at:',match.start())
    print('group is :',match.group())



