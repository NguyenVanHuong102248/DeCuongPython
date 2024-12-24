import math

n = int(input())
S = 0
for i in range(0, n + 1):
    S += math.factorial(2 * i + 1)
S += 1
print("S = {}".format(S))
