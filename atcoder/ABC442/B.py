Q = int(input())
ans = 0
nowplay = False
for i in range(Q):
    val = int(input())
    if val ==1:
        ans+=1
    elif val==2:
        if ans>=1: ans-=1
    elif val==3:
        nowplay = not nowplay

    if nowplay and ans>=3: print('Yes')
    else: print('No')
