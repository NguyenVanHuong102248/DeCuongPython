m, n = map(int,input().split())
a = []
for _ in range(m):
    row = list(map(int, input().split()))
    a.append(row)
b = []
for i in range(m):
    if sum(a[i]) % 7 == 0:
        b.append(i+1)
if b:
    print(" ".join(map(str,b)))
else:
    print("NO")

