n,m = [int(i) for i in input().split(' ')]
# a = int(input())
A, B = [0]*n, [0]*n
for j in range(n):
    A[j], B[j] = [int(i) for i in input().split(' ')]

ls = [[] for i in range(m+1)]
for i in range(n):
    ls[A[i]].append(B[i])

# print(ls)

for val in ls[1:]:
    # print(val)
    print(sum(val)/len(val))