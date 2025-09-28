n, m = [int(i) for i in input().split(' ')]


num = [[] for i in range(m)]
for _ in range(n):
    s = list(input())

    for i, c in enumerate(s):
        num[i].append(int(c))

# print(num)

points = [0]*n
for id, s in enumerate(num):
    if sum(s) >int((n-1)/2):
        for i in range(n):
            if s[i]==0: points[i]+=1
    else:
        for i in range(n):
            if s[i]==1: points[i]+=1
out = []
max_val = max(points)

for i in range(n):
    if points[i]==max_val: 
        out.append(str(i+1))
# print(out)
print(' '.join(out))