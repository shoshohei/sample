from collections import deque
n = int(input())
dep = [[] for i in range(n+1)]
get_skill_id  =[False]*(n+1)
q = deque()

for i in range(1, n+1):
    a, b = [int(i) for i in input().split(' ')]
    if a==0 and b==0:
        get_skill_id[i] = True
        q.append(i)
    else:
        if a!=0:
            dep[a].append(i)
        if b!=0:
            dep[b].append(i)

while q:
    cur = q.popleft()
    for n in dep[cur]:
        if not get_skill_id[n]:
            get_skill_id[n] = True
            q.append(n)

print(sum(get_skill_id))