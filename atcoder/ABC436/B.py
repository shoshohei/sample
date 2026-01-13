n = int(input())
out = [[0]*n for _ in range(n)]
val = 1
out[0][(n-1)//2] = val
val += 1 
pre_raw, pre_col = 0, (n-1)//2
for i in range(n**2-1):
    print(pre_raw, pre_col)
    row, col = (pre_raw-1)%n, (pre_col+1)%n
    if out[row][col] != 0:
        out[row][col] = val
        val += 1
        pre_raw, pre_col = row, col
        continue
    row, col = (pre_raw+1)%n, pre_col
    out[row][col] = val
    val += 1
    pre_raw, pre_col = row, col
    
    
for i in range(len(out)):
    out[i] = [str(j) for j in out[i]]
    print(' '.join(out[i]))


