n = int(input())
A = [int(i) for i in input().split(' ')]

# check_num = [False]*(n)
# for i in range(n):
#     if i%int(1e9+7)==0: check_num[i]=True

accum = [0]*(n+1)
for i in range(n):
    accum[i+1] = accum[i]+A[i]

reverse_accum = [0]*(n+1)
for i in range(n):
    reverse_accum[i+1] = reverse_accum[i]+A[n-1-i]

# print(accum, reverse_accum)

sum = 0
for i in range(n):
    # print(A[i], reverse_accum[n-1-i])
    sum += A[i]*reverse_accum[n-1-i]

print(sum%(int(1e9+7)))