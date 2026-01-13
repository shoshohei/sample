n,m,k = [int(i) for i in input().split(' ')]
H = [int(i) for i in input().split(' ')]
B = [int(i) for i in input().split(' ')]
H.sort()
B.sort()
count = 0
out = 'No'
H_offset = 0
B_offset = 0
while out=='No':
    if H[H_offset] <= B[B_offset]:
        # print(H[H_offset] , B[B_offset])
        count += 1
        H_offset += 1
        B_offset += 1
    else:
        B_offset += 1
    if count >=k: 
        out = 'Yes'
        break
    if H_offset >= len(H): break
    if B_offset >= len(B): break

print(out)