N=int(input())
A=[int(i) for i in input().split(' ')]
ls = [0 for _ in range(N+1)]
# print(A,ls)
for i in A:
#   print(ls[i])
  ls[i] += 1
bool_ls = [True]*(N+1)
for i in ls:
  if i==0:
    bool_ls[i] = False
bool_sum = sum(bool_ls)
# K = max(ls)
# binom = [[0] * (K+1) for i in range(K+1)]
# binom[0][0] = 1
# for n in range(1, K+1):
#     binom[n][0] = 1
#     for k in range(1, n + 1):
#         binom[n][k] = (binom[n - 1][k - 1] + binom[n - 1][k])
# print(binom)
count = 0
# print(K, ls, bool_sum)
for i in ls:
  if i>=2:
    # print(i, binom[i][2], bool_sum-i)
    # count += binom[i][2]*(bool_sum-i)
    count += i*(i-1)//2*(bool_sum-i)
print(count)