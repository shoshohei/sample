n = int(input())
A = [int(i) for i in input().split(' ')]
stack = []
for a in A:
    if stack and stack[-1][0]==a:
        val, num = stack.pop()
        num += 1
        if num!=4:
            stack.append((val, num))
    else:
        stack.append((a, 1))
res = sum(num for _,num in stack)
print(res)