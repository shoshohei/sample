n,m= [int(i) for i in input().split(' ')]
s = list(input())
t = list(input())
Q = int(input())

bool_s = {}
bool_t = {}

for c in s: bool_s[c] = True
for c in t: bool_t[c] = True
    
for _ in range(Q):
    q = list(input())
    sCount, tCount = 0, 0
    for c in q:
        if bool_s.get(c, False): sCount += 1
        if bool_t.get(c, False): tCount += 1
    # print(sCount, tCount)
    if sCount == len(q) and tCount == len(q): print('Unknown')
    elif sCount ==len(q): print('Takahashi')
    elif tCount==len(q): print('Aoki')
    else: print('Unknown')