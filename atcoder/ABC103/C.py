from functools import reduce
import math
n = int(input())
A = [int(i) for i in input().split(' ')]
temp = 0
for val in A [1:]:
    temp = temp*val//math.gcd(temp, val)

lcm_all = temp
sum = 0
lcm_all-=1
for a in A:
    sum += lcm_all%a
print(sum)