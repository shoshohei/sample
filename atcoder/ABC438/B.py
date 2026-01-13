n, m = [int(i) for i in input().split(' ')]
S = list(input())
T = list(input())

len_T = len(T)
ls_S = []
i=0
while i+len_T<=len(S):
    ls_S.append(S[i:i+len_T])
    i+=1
# print(ls_S)
res = 10**10
for l in ls_S:
    score = 0
    for i in range(len_T):
        index = -i-1
        s, t = int(l[index]), int(T[index])
        if s<t:
            s+=10
        score += s-t
    res = min(res, score)

print(res)