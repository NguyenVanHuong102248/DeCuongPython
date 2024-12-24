n = int(input())
S = 0
for i in range(1, n + 1):
    S += 1 / (i * (i + 1))
print("S = {:.6f}".format(S))
