n = int(input())
U, D, L, R = [0]*n, [0]*n, [0]*n, [0]*n
for i in range(n):
    U[i], D[i], L[i], R[i] = [int(i) for i in input().split(' ')]
max_len_num = max(max(D), max(R))+1
maps = [[0]*(max_len_num+1) for i in range(max_len_num+1)]
for i in range(n):
    maps[U[i]][L[i]] += 1
    maps[U[i]][R[i]+1] -= 1
    maps[D[i]+1][L[i]] -= 1
    maps[D[i]+1][R[i]+1] += 1

accum_maps = [[0]*(max_len_num+1) for i in range(max_len_num+1)]
for i in range(max_len_num):
    for j in range(1, max_len_num+1):
        maps[i][j] += maps[i][j-1]
for j in range(max_len_num):
    for i in range(1, max_len_num+1):
        maps[i][j] += maps[i-1][j]

is1 = [[0]*(max_len_num+1) for _ in range(max_len_num+1)]
for i in range(max_len_num+1):
    for j in range(max_len_num+1):
        is1[i][j] = 1 if maps[i][j] == 1 else 0
# for i in is1:
#     print(f'{''.join([str(j) for j in i])}')
IS1 = [[0]*(max_len_num+2) for _ in range(max_len_num+2)]
for i in range(1, max_len_num+2):
    for j in range(1, max_len_num+2):
        IS1[i][j] = (
            is1[i-1][j-1]
            + IS1[i-1][j]
            + IS1[i][j-1]
            - IS1[i-1][j-1]
        )
# for i in IS1:
#     print(f'{' '.join([str(j) for j in i])}')
# exit()
count = 0
for i in range(1, max_len_num+1):
    for j in range(1, max_len_num+1):
        if maps[i][j] == 0: count += 1
total_num = 2000*2000-max_len_num**2+count

def rect_sum(S, x1, y1, x2, y2):
    x1+=1
    # y1+=1
    # print(S[y2+1][x2+1],S[y1][x2+1], S[y2+1][x1],S[y1][x1])
    return (
        S[y2+1][x2+1]
        - S[y1][x2+1]
        - S[y2+1][x1]
        + S[y1+1][x1]
    )
for i in range(n):
    # print(L[i], U[i], R[i], D[i])
    kaburi = rect_sum(IS1, L[i], U[i], R[i], D[i])
    area = (D[i]+1-U[i])*(R[i]+1-L[i])
    # print(kaburi, area)
    print(total_num+area-kaburi)
