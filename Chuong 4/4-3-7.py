n = int(input())
a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[n-i-1][n-1-i]
print("Tong duong cheo chinh: ",sum1)
print("Tong duong cheo phu: ",sum2)
