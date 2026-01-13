n,k = [int(i) for i in input().split(' ')]
nums = []
while n>0:
    nums.append(str(n%k))
    n = n //k
print(len(nums))