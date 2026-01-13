n, x, y = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]

out = 0
Ax = [a*x for a in A]
Ay = [a*y for a in A]
min_Ay = min(Ay)
max_Ax = max(Ax)
if min_Ay<max_Ax:
    out = -1
else:
    A_mod = [a%(y-x) for a in Ax]
    if len(set(A_mod))!=1: out = -1
    else:
        K = min_Ay-(min_Ay-A_mod[0])%(y-x)
        out = (n*K-x*sum(A))/(y-x)
print(int(out))