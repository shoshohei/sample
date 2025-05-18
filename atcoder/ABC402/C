from collections import defaultdict
[n, m] = [int(i) for i in input().split(' ')]
k = []
A = []
values = defaultdict(list)
for i in range(m):
    ls = [int(i) for i in input().split(' ')]
    k.append(ls[0])
    A.append(ls[1:])
    for j in ls[1:]:
        values[j].append(i)
b = [int(i) for i in input().split(' ')]


res = 0
boo = [False]*m
for i in b:
    for j in values.get(i, []):
        if not boo[j]:
            k[j]-=1
            if k[j]==0:
                res+=1
                boo[j] = True
    print(res)
