T = int(input())

def comfirm_square():
    result = False
    print(i,j)
    if S[i][j]=='#':
        if S[i-1][j-1]=='#' and S[i-1][j]=='#' and S[i][j-1]=='#':
            result = True
        elif S[i-1][j]=='#' and S[i-1][j+1]=='#' and S[i-1][j+1]=='#':
           result = True
        elif S[i+1][j]=='#' and S[i+1][j-1]=='#' and S[i][j-1]=='#':
           result = True
        elif S[i+1][j]=='#' and S[i+1][j+1]=='#' and S[i][j+1]=='#':
           result = True
    return result



for t in range(T):
    count = 0
    h,w = [int(i) for i in input().split(' ')]
    S = []
    for i in range(w):
        S.append(list(input()))
    print(S)
    for i in range(1,h-1):
        for j in range(1,w-1):
            if comfirm_square():
                S[i][j] = '.'
                count += 1
    print(count)