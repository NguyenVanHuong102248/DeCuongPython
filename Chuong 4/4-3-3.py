m, n, p = map(int,input().split())
matrix1 = []
matrix2 = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix1.append(row)
for _ in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)
matrix_tich = []
for i in range(m):
    row_tich = []
    for j in range(n):
        sum = 0
        for k in range(n):
            sum += matrix1[i][k] * matrix2[k][j]
        row_tich.append(sum)
    matrix_tich.append(row_tich)
for row in matrix_tich:
        print(' '.join(map(str, row)))
