n, m, k = [int(i) for i in input().split(' ')]
acc = [0]*n
acc_p = []

for i in range(k):
    a, b = [int(i) for i in input().split(' ')]
    acc[a-1] += 1
    # print(acc)
    if acc[a-1]==m:
        acc_p.append(str(a))
    
print(' '.join(acc_p))