N, Q = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]

def swap(ls, id):
    temp = ls[id]
    ls[id] = ls[id+1]
    ls[id+1] = temp
    return ls

now_A = A.copy()
prefix = [0]*(N+1)
for i in range(N):
    prefix[i+1] = prefix[i]+A[i]
diff = [0]*(N+1)
for i in range(Q):
    q = [int(i) for i in input().split(' ')]
    if q[0]==1:
        x = q[1]
        x-= 1
        diff[x+1] += now_A[x+1]-now_A[x]
        diff[x+2] += now_A[x]-now_A[x+1]
        now_A = swap(now_A, x)
        print(diff, now_A)
    else:
        l,r = q[1:]
        val = prefix[r]-prefix[l-1] + diff[r]+diff[l]
        print(prefix[r], prefix[l-1] , diff[r], diff[l])
        print(val)