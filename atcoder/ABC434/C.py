T = int(input())

def my_clamp(val, min, max):
    if val<min: return min-val
    elif val>max: return max-val
    else: return 0

for i in range(T):
    n,h = [int(i) for i in input().split(' ')]
    t,l,u = [0]*n, [0]*n, [0]*n
    for j in range(n):
        t[j],l[j],u[j] = [int(i) for i in input().split(' ')]
    