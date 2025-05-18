n = int(input())
S = [input() for s in range(n)]
islogin = False
err_count = 0

for i in S:
    if i == 'login':
        islogin = True
    elif i == 'logout':
        islogin = False
    if islogin is False and i == 'private':
        err_count+=1
print(err_count)