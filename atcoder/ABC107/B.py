h, w = [int(i) for i in input().split(' ')]
A = [list(input()) for i in range(h)]
S = [[0]*w for i in range(h)]

for i in range(h):
    for j in range(w):
        if A[i][j]=='#':
            S[i][j] = 1

S_omitted = []
for i in range(h):
    if sum(S[i])!=0:
        S_omitted.append(S[i])


import numpy as np
S_T = np.transpose(S_omitted)
# print(S_omitted, S_T)
S_T_omitted = []
for i in range(len(S_T)):
    if sum(S_T[i])!=0:
        S_T_omitted.append(S_T[i])

res_bool = np.transpose(S_T_omitted)

res_h, res_w = len(res_bool), len(res_bool[0])
res = [['.']*res_w for i in range(res_h)]
# print(res)
for i in range(res_h):
    for j in range(res_w):
        if res_bool[i][j]==1:
            res[i][j] = '#'
for i in range(res_h):
    print(''.join(res[i]))