m, n = map(int, input().split())
a = []
for _ in range(m):
    row = list(map(int, input().split()))
    a.append(row)
sum1 = 0
total = m * n
for row in a:
    sum1 += sum(row)
average = sum1 / total
print("{:.2f}".format(average))
for i in range(m):
    for j in range(n):
        if a[i][j] > average:
            print(a[i][j], i + 1, j + 1)
