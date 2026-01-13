import sys
input = sys.stdin.readline
from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for _ in range(Q):
    X, Y = map(int, input().split())
    
    # Aの中で X 以上の最初の位置
    base = bisect_left(A, X)
    
    # 「X以上k以下に存在しない数の個数」
    def missing(k):
        # Aの中で k 以下の個数 - X以上の個数
        cnt = bisect_left(A, k + 1) - base
        return (k - X + 1) - cnt
    
    # 二分探索
    ng = X - 1
    ok = X + Y + N  # 十分大きい上限
    
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if missing(mid) >= Y:
            ok = mid
        else:
            ng = mid
    
    print(ok)
