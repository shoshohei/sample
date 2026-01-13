n = int(input())
W, H, B = [], [], []
for i in range(n):
    w,h,b = [int(i) for i in input().split(' ')]
    W.append(w)
    H.append(h)
    B.append(b)
max_diff = max(W)*n
offset = max_diff
dp = [-float('inf')]*(2*max_diff+1)
dp[offset] = 0
for id, (w,h,b) in enumerate(zip(W,H,B)):
    next_dp = [-float('inf')]*(2*max_diff+1)
    for d in range(2*max_diff+1):
        if dp[d]==-float('inf'): continue
        delta = d-offset
        # body
        nd_body = delta - w + offset
        if 0 <= nd_body < 2 * max_diff + 1:
            next_dp[nd_body] = max(next_dp[nd_body], dp[d] + b)
        # head
        nd_head = delta + w + offset
        if 0 <= nd_head < 2 * max_diff + 1:
            next_dp[nd_head] = max(next_dp[nd_head], dp[d] + h)
    dp = next_dp

print(max(dp[:offset+1]))

# from collections import defaultdict
# dp = defaultdict(lambda : -float('inf'))
# dp[0] = 0
# for id, (w, h, b) in enumerate(zip(W, H, B)):
#     next_dp = defaultdict(lambda : -float('inf'))
#     for delta, val in dp.items():
        
#         # bodyに
#         # print(next_dp[delta+b], dp[delta]+b)
#         next_dp[delta-w] = max(next_dp[delta-w], dp[delta]+b)
#         # headに
#         next_dp[delta+w] = max(next_dp[delta+w], dp[delta]+h)
#         # print(next_dp[delta+w], dp[delta]+h)
#     dp = next_dp


# max_ = -1e6
# for delta, val in dp.items():
#     if max_ < val and delta <= 0:
#         max_ = val
# print(max_)