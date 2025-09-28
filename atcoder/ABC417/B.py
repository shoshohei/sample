n, m = [int(i) for i in input().split(' ')]
a = [int(i) for i in input().split(' ')]
b = [int(i) for i in input().split(' ')]
for i in b:
    if i in a:
        a.remove(i)
s = ''
for i in a:
    s = s+str(i)+' '


if s!='':print(s)