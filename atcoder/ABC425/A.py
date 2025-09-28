n = int(input())
sum = 0
di = -1
for i in range(1,n+1):
    sum += di*(i**3)
    di *= -1
print(sum)