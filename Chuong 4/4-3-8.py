n = int(input())
upper = True
lower = True

a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
for i in range(n):
    for j in range(i+1,n):
        if a[i][j] != 0:
            upper = False
            break
    if not upper:
        break
for i in range(n):
    for j in range(i):
        if a[i][j] != 0:
            lower = False
            break
    if not lower:
        break
if lower:
    print("LOWER TRIANGLE")
elif upper:
    print("UPPER TRIANGLE")
else:
    print("NONE")