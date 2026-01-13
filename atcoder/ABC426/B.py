S = list(input())
idx = -1
for id, c in enumerate(S[:-2]):
    if S[id]!=S[id+1]:
        idx = id+1
        break
if idx == 1:
    if S[idx]==S[idx+1]:
        idx = 0
print(S[idx])