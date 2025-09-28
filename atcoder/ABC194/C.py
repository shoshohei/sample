n = int(input())
A = [int(i) for i in input().split(' ')]

sum_square = 0
for a in A:
    sum_square += a**2

reverse_accum = [0]*(n+1)
for i in  range(n):
    reverse_accum[i+1] = reverse_accum[i]+A[n-1-i]
# print(reverse_accum)
mul_A = 0
for i in range(n-1):
    # print(A[i], reverse_accum[n-1-i])
    mul_A += A[i]*reverse_accum[n-1-i]

# print(sum_square, mul_A)
print((n-1)*sum_square-2*mul_A)

