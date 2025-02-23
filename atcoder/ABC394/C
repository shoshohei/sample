# def my_find(s):
#     for i in range(len(s)-1):
#         if s[i]=="W" and s[i+1]=="A":
#             return i
#     return -1

# s = list(input())
# while True:
#     index = my_find(s)
#     if index>-1:
#         s[index]="A"
#         s[index+1]="C"
#     else:
#         break
# print("".join(s))

s=list(input())
n=len(s)
i=1
while i<n:
    if s[i-1]=='W' and s[i]=='A':
        s[i-1], s[i]='A', 'C'
        i-=1
        i=max(1,i)
    else:
        i += 1
print("".join(s))