from collections import deque
q = int(input())

A = deque()
B = deque()
A.append(0)
B.append(0)
for _ in range(q):
    ls = input().split(' ')
    if ls[0]=='1':
        val = 1 if ls[1]=='(' else -1
        A.append(A[-1]+val)
        B.append(min(B[-1], A[-1]))

    else:
        A.pop()
        B.pop()
    

    if A[-1]==0 and B[-1]>=0: print('Yes')
    else: print('No')
