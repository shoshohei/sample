n = int(input())
A = [0] + [int(i) for i in input().split(' ')]
full_visited = [0]*(n+1)

for i in range(1, n+1):
    # if i==3: exit()
    if full_visited[i]: continue
    # visited = [False]*(n+1)
    path = []
    pos = {}
    cur = i
    while True:
        if full_visited[cur]:
            ans = full_visited[cur]
            for v in path:
                full_visited[v] = ans
            break
        if cur in pos:
            cycele_first = pos[cur]
            cycle = path[cycele_first:]
            for v in cycle:
                full_visited[v] = cur
            
            for v in path[:cycele_first]:
                full_visited[v] = cur
            # print(i, cur, cycele_first, cycle, full_visited)
            break
        pos[cur] = len(path)
        path.append(cur)
        cur = A[cur]
        # print(pos,path, full_visited)



print(' '.join([str(i) for i in full_visited[1:]]))