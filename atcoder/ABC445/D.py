h, w, N = map(int, input().split())

H = [0]*N
W = [0]*N

mapH = {}
mapW = {}

for i in range(N):
    H[i], W[i] = map(int, input().split())
    mapH[H[i]] = i
    mapW[W[i]] = i

used = [False]*N
pos = ['']*N

while h > 0 and w > 0:

    if h in mapH and not used[mapH[h]]:
        i = mapH[h]
        used[i] = True
        w -= W[i]
        pos[i] = f'1 {w+1}'

    elif w in mapW and not used[mapW[w]]:
        i = mapW[w]
        used[i] = True
        h -= H[i]
        pos[i] = f'{h+1} 1'

    else:
        break



for p in pos: print(p)
