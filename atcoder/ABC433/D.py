n, m = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]

def check_digit(num):
    digit = 1
    while num//10!=0:
        num//=10
        # print(num)
        digit += 1
    # print(digit)
    return digit
# print(check_digit(123))
digit_A = [check_digit(a) for a in A]
# print(digit_A)
# digit_10 = {}
# for i in range(1, max(digit_A)+1):
#     digit_10[i] = [0]*m

# for key, value in digit_10.items():
#     val = 10**key
#     for a in A:
#         digit_10[key][(a*val)%m] += 1
digit_10 = {d: {} for d in set(digit_A)}

for a in A:
    a_mod = a % m
    for d in digit_10.keys():
        key = (a_mod * pow(10, d, m)) % m
        digit_10[d][key] = digit_10[d].get(key, 0) + 1
count = 0
for a in A:
    val = m-(a%m)
    if val==m: val=0
    count += digit_10[check_digit(a)].get(val, 0)

print(count)