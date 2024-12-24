import math

x = float(input())
n = int(input())
S = 0

for _ in range(n):
    S = math.sqrt(x + S)

S += 1
print("S = {:.6f}".format(S))
