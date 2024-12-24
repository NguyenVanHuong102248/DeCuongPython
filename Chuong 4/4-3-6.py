n = int(input())
a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
count = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == a[j][i]:
            count += 1
if count == n*n:
    print("YES")
else:
    print("NO")