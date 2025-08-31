def rev_val(num1, num2):
    num = num1 + num2
    num_s = list(str(num))
    num_s.reverse()
    rev_num_s = num_s
    # print(rev_num_s)
    idx = -1
    for id, c in enumerate(rev_num_s):
        if c!='0':
            idx = id
            break
    # print(rev_num_s[idx:])
    return int(''.join(rev_num_s[idx:])) 

x, y = [int(i) for i in input().split(' ')]

A = [0 for _ in range(10)]
A[0] = x
A[1] = y
for i in range(2, 10):
    A[i] = rev_val(A[i-1], A[i-2])

print(A[-1])