h ,w = [int(i) for i in input().split(' ')]
S = [list(input()) for i in range(h)]

def in_grid(x,y):
    return 0<=x<h and 0<=y<w

def count(x, y):
    c = 0
    for dx, dy in dxy:
        nx, ny = x+dx, y+dy
        if in_grid(nx, ny) and S[nx][ny]=='#':
            c += 1
    return c

# for i in range(h):
#     for j in range(w):
#         # print(i*w+j)
#         if S[i][j] == '#': 
#             q.append(i*w+j)
#             flat_S_bool[i*w+j] = 1

dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for i in range(h*w):
    if i==0:
        q = []
        for x in range(h):
            for y in range(w):
                if S[x][y]=='.' and count(x, y)==1:
                    q.append((x, y))

    else:
        nq = []
        for x, y in q:
            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if in_grid(nx, ny) and S[nx][ny]=='.' and count(nx, ny)==1:
                    nq.append((nx, ny))
        q = nq
    
    if len(q)==0: break
    for x, y in q:
        S[x][y] = '#'

ans = 0
for x in range(h):
    for y in range(w):
        ans += int(S[x][y] == "#")
print(ans)