# T = int(input())

# for t in range(T):
#     n, w = [int(i) for i in input().split(' ')]
#     C = [int(i) for i in input().split(' ')]
#     for i in range(1,n+1):
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, W = map(int, input().split())
    C = list(map(int, input().split()))
    
    M = 2 * W
    arr = [0] * M
    
    for i in range(N):
        arr[i % M] += C[i]
    
    arr2 = arr + arr
    
    cur = sum(arr2[:W])
    ans = cur
    
    for l in range(1, M):
        cur += arr2[l + W - 1]
        cur -= arr2[l - 1]
        if cur < ans:
            ans = cur
    
    print(ans)
