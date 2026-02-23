n = int(input())
s = list(input())

S = []
for c in s:
    val = 0
    if c=='A':
        val = 1
    if c=='B':
        val = -1
    S.append(val)
accum = [0]*(n+1)
for i in range(n):
    accum[i+1] = accum[i]+S[i]
    
# print(S, accum)
for i in range(n):
    for j in range(i,n):
        