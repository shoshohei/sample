n, r = map(int, input().split())
isLock = list(map(int, input().split()))

# 左端から閉まっている扉の最初
x = 0
while x < n and isLock[x] == 1:
    x += 1

# 右端から閉まっている扉の最後
y = n - 1
while y >= 0 and isLock[y] == 1:
    y -= 1

# R を基準に左右の操作を計算
open_doors = 0  # 開操作の回数
move_ops = 0    # 移動＋閉操作の回数

# 左側
if x <= r - 1:
    # ドア x … R-1 の閉まっている扉を開ける
    left_range = isLock[x:r]
    open_doors += sum(1 for d in left_range if d == 1)
    # 区間長さは閉操作＋移動回数に寄与
    move_ops += len(left_range)

# 右側
if y >= r:
    # ドア R … y の閉まっている扉を開ける
    right_range = isLock[r:y+1]
    open_doors += sum(1 for d in right_range if d == 1)
    move_ops += len(right_range)

# 最終操作回数 = 開操作 + 閉操作（閉操作 = 移動＋開けた扉含む区間）
ans = open_doors + move_ops

# すべて閉まっている場合
if sum(isLock) == n:
    ans = 0

print(ans)
