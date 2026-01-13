t = int(input())
N, S = [0]*(t), ['']*t
# print(N,S)
for i in range(t): 
    N[i], S[i] = int(input()), list(input())
    S[i] = [True if i=='1' else False for i in S[i]]

for i in range(t):
    out = 'Yes'
    n, s = N[i], S[i]
    # print(n,s)
    # S[i].reverse()
    count = 0
    for j in range(1, n+1):
        val = 2**(j-1)
        # print(val, s[val-1])
        if s[val-1]: 
            count += 1
    # print(count, n)
    if count==n:
        print('No')
        continue
    count = 0
    for j in range(1, n+1):
        for k in range(j+1, n+1):
            val = 2**(j-1)+2**(k-1)
            # print(val, s[val-1])
            if s[val-1]:
                count += 1
                
    # print(count, n, n*(n-1)//2, out)
    if count==n*(n-1)//2:
        out = 'No'
    print(out)