m, n, k = map(int, input().split())
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
count = 0
for row in matrix:
    count += row.count(k)
print(count)
