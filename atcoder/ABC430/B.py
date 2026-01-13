n,m = [int(i) for i in input().split(' ')]
S = [list(input()) for i in range(n)]
bool_S = [[False]*n for i in range(n)]

for i, s in enumerate(S):
    for j, c in enumerate(s):
        # print(i,j)
        if c=='#':
            bool_S[i][j] = True
# print(bool_S)
M = []
for i in range(n-m+1):
    for j in range(n-m+1):
        C = [tuple(s[j:j+m]) for s in bool_S[i:i+m]]
        C = tuple(C)
        # print(C)
        M.append(C)
# M = tuple(M)
print(len(set(M)))