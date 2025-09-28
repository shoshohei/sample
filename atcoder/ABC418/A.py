n = int(input())
s = input()
s = list(s)
out = 'No'
if ''.join(s[-3:])=='tea':
    out = 'Yes'
print(out)