n = int(input())
A = [int(i) for i in input().split(' ')]
bool_A = []
for i in range(n):
    if A[i]!=-1:
        bool_A.append(A[i])
# print(bool_A)
if len(bool_A)!=len(set(bool_A)):
    print('No')
else:
    bool_A = list(set(range(1,n+1))-set(bool_A))
    out_nums = [] 
    for i in range(n):
        if A[i]==-1:
            val = bool_A.pop()
        else:
            val = A[i]
        out_nums.append(str(val))
    print('Yes')
    print(' '.join(out_nums))

