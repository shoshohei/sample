<<<<<<< HEAD
num = input().split(' ')
n, m = [int(i) for i in num]
b = [int(i) for i in input().split(' ')]
w = [int(i) for i in input().split(' ')]

b.sort(reverse=True)
w.sort(reverse=True)
# print(b)
# print(w)
# w_bool = [i>0 for i in w]
# w_plus = sum(w_bool)
# print(w_plus)
# exit()

res = 0
for i in range(min(n, m)):
    if res+b[i]>=res:
        res+=b[i]
        if res+w[i]>=res:
            res+=w[i]
    elif res+b[i]+w[i]>=res:
        res+=b[i]+w[i]
while True:
    i+=1
    if i>=n:
        break
    if b[i]>=0:
        res+=b[i]
=======
num = input().split(' ')
n, m = [int(i) for i in num]
b = [int(i) for i in input().split(' ')]
w = [int(i) for i in input().split(' ')]

b.sort(reverse=True)
w.sort(reverse=True)
# print(b)
# print(w)
# w_bool = [i>0 for i in w]
# w_plus = sum(w_bool)
# print(w_plus)
# exit()

res = 0
for i in range(min(n, m)):
    if res+b[i]>=res:
        res+=b[i]
        if res+w[i]>=res:
            res+=w[i]
    elif res+b[i]+w[i]>=res:
        res+=b[i]+w[i]
while True:
    i+=1
    if i>=n:
        break
    if b[i]>=0:
        res+=b[i]
>>>>>>> 660d0d0f24734efffae7e8823a1955937c02e1a1
print(res)