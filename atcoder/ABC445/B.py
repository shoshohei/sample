n = int(input())
S = ['']*n
max_len = 0
for i in range(n):
    S[i] =input()
    if len(S[i])>=max_len:
        max_len = len(S[i])

for i in range(n):
    s = S[i]
    num = (max_len-len(S[i]))//2
    print('.'*num + s + '.'*num)
