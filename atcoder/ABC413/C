q = int(input())

A = []
vals = []
val_num = []
sum_ = 0
first_id = 0
import bisect
for _ in range(q):
    ls = [int(i) for i in input().split(' ')]
    if ls[0]==1:
        sum_ += ls[1]
        val_num.append(sum_)
        vals.append(ls[2])

    else:
        end_id = first_id+ls[1]
        first_pos = bisect.bisect_right(val_num, first_id)
        end_pos = bisect.bisect_right(val_num, end_id)
        # print(first_pos, first_id, end_pos, end_id, vals, val_num, sum_)
        
        out = 0
        out += (val_num[first_pos] - first_id) * (vals[first_pos]) # 個数×値
        # print(out)
        out += vals[end_pos]*(end_id-val_num[end_pos-1]) # 値×個数
        print(out)
        first_id = end_id
