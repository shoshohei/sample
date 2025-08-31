def swap(a, b):
    temp = P[a]
    P[a] = P[b]
    P[b] = temp

n = int(input())
P = [int(i) for i in input().split(' ')]

id = -1
for i in range(n-1):
    if P[-(1+i)]<P[-(2+i)]:
        id = n-i-1
        break

candiadte_nums = P[id:]
conditional_max_val = 0
conditional_max_id = n+1 
for i, num in enumerate(candiadte_nums):
    if P[id-1]>num and conditional_max_val<num:
        conditional_max_val = num
        conditional_max_id = id+i

# print(id, candiadte_nums, conditional_max_id, conditional_max_val)
swap(id-1, conditional_max_id)
# print(P)

P[id:] =  sorted(P[id:], reverse=True)
# print(P)
out = ''
for p in P[:-1]:
    out = out + str(p) + ' '
    # print(out)
print(out+str(P[-1]))