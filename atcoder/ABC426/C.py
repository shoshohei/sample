n, q = [int(i) for i in input().split(' ')]
X, Y = [], []
for i in range(q):
    x, y = [int(i) for i in input().split(' ')]
    X.append(x)
    Y.append(y)

pc = [1]*(n+1) # それぞれの端末の個数
old = 1 # 今ある端末の中で最古のもの
# for i in range(q):
#     x, y = X[i], Y[i]
#     out = 0
#     while old<=x:
#         out += pc[old]
#         pc[y] += pc[old]
#         old+=1
#     print(pc[1:])
#     print(out)

for i in range(q):
    x, y = X[i], Y[i]
    res = 0
    for j in range(old, x+1):
        res += pc[j]
        pc[y] += pc[j]
        old += 1
    print(res)
