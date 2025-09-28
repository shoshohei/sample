n, k, x = [int(i) for i in input().split(' ')]
S = [input() for _ in range(n)]
F= []
if k==1:
    for i in range(n):
        F.append(S[i])
elif k==2:
    for i in range(n):
        for j in range(n):
            F.append(S[i]+S[j])
elif k==3:
    for i in range(n):
        for j in range(n):
            for l in range(n):
                F.append(S[i]+S[j]+S[l])
elif k==4:
    for i in range(n):
        for j in range(n):
            for l in range(n):
                for m in range(n):
                    F.append(S[i]+S[j]+S[l]+S[m])
elif k==5:
    for i in range(n):
        for j in range(n):
            for l in range(n):
                for m in range(n):
                    for o in range(n):
                        F.append(S[i]+S[j]+S[l]+S[m]+S[o])

F.sort()
print(F[x-1])