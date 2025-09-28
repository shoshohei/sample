n, k = [int(i) for i in input().split(' ')]
from collections import deque
from collections import defaultdict
in_num = 0
wait_q = deque()
times = defaultdict(int)
for i in range(n):
    ls = [int(i) for i in input().split(' ')]
    wait_q.append(ls)
    a, b, c = ls
    times[a+b] += c
    # tiems = dict(sorted(times.items()))
    first_key, first_value = next(iter(times.items()))
    if first_key<=b:
        in_num -= first_value
        times.pop(first_key)
        
    print(in_num, times)
    if in_num+c<=k:
        in_num += c
        print(a)
    else:
        ls = list(times.keys())
        for id,key in enumerate(ls):
            if key>a:
                break
        print(ls[id-2])