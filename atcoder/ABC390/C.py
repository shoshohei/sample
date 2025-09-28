h, w = [int(i) for i in input().split(' ')]
S = []
for _ in range(h):
    S.append(input())
x=y=0
for y in range(h):
    for x in range(w):
        if S[y][x]=='#':
            break
end_x = 0
pre_char = '#'
for end_x in range(x+1, h):
    if S[y][end_x] == '.': 
        end_x -= 1
        break
    elif S[y][end_x] == '#' or S[y][end_x] == '?':
