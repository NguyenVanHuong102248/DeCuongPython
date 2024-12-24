x = float(input())
n = int(input())
S = 0
for i in range(1, n + 1):
    S += x**i
print("S = {}".format(S))
