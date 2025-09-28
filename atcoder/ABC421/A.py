n = int(input())
S = [input() for _ in range(n)]
x, y = [i for i in input().split(' ')]
out = 'No'
if S[int(x)-1]==y:
    out = 'Yes'
print(out)