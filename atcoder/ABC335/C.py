from collections import deque
n ,q = [int(i) for i in input().split(' ')]
pos_ls = []
to_dir = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
for i in range(1,n+1):
    pos_ls.append((n+1-i,0))

for _ in range(q):
    q_num, val = input().split(' ')
    if q_num=='1':
        head_pos = pos_ls[-1]
        pos_ls.append((head_pos[0]+to_dir[val][0], head_pos[1]+to_dir[val][1]))
    else:
        out = pos_ls[-int(val)]
        out = [str(i) for i in out]
        print(' '.join(out))