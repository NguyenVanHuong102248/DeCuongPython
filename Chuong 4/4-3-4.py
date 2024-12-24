m, n = map(int,input().split())
matrix1 = []
matrix2 = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix1.append(row)
for _ in range(m):
    row = list(map(int, input().split()))
    matrix2.append(row)
matrix_sum = []
for i in range(m):
    row_sum = []
    for j in range(n):
        row_sum.append(matrix1[i][j] + matrix2[i][j])
    matrix_sum.append(row_sum)
for i in matrix_sum:
    print(" ".join(map(str,i)))