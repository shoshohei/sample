
h, w, n = [int(i) for i in input().split(' ')]
A = []
for i in range(h): A.append([int(i) for i in input().split(' ')])
B = [int(input()) for _ in range(n)]
val = [0]*h
for i in range(h):
    count = 0
    for j in range(n):
        if B[j] in A[i]: count+=1
    val[i] = count

print(max(val))