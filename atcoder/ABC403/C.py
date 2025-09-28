
[x, y, q] = [int(i) for i in input().split(' ')]
state = [set() for _ in range(x)]
state_all = [False]*x

for i in range(q):
    ls = [int(i) for i in input().split(' ')]
    a = ls[1]-1
    if ls[0]==1:
        b = ls[2]-1
        state[a].add(b)
    elif ls[0]==2:
        state_all[a] = True
    elif ls[0]==3:
        b = ls[2]-1
        if b in state[a] or state_all[a]:
            print('Yes')
        else:
            print('No')