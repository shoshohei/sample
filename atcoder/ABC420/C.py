n, q = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]
B = [int(i) for i in input().split(' ')]

min_ls = [min(a, b) for a, b in zip(A, B)]
min_sum = sum(min_ls)

for i in range(q):
    c, x, v = [i for i in input().split(' ')]
    x = int(x)
    v = int(v)
    
    out = min_sum - min_ls[x-1]
    # print(out)
    if c=='A':
        min_ls[x-1]= min(B[x-1], v)
        A[x-1] = v

    elif c=='B':
        min_ls[x-1]= min(A[x-1], v)
        B[x-1] = v

    out += min_ls[x-1]
    min_sum = out

    print(out)

