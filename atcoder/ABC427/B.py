n = int(input())
A = [1]*(n+1)

for i in range(n):
    num = A[i]
    if len(str(num))!=1:
        s = str(num)
        s = [c for c in list(s)]
        ls = [int(j) for j in s]
        val = sum(ls)
    else: val = num
    A[i+1] = A[i] + val
print(A[-2])