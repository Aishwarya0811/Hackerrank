import re
str1="{I am|I'm} {working on|starting} this {online |}interview. I hope Cortx thinks I am {{very|extremely} qualified|great|awesome}{!|.}"
str1
p=re.split('{|}',str1)
p
b = []
for i in p:
    if '|' in i:
        b.append(i.split('|')[0])
    else:
        b.append(i)

''.join(i for i in b)
