import math

n = 1
S = 1
while S <= 1000:
    n += 1
    S += 1 / math.factorial(2 * n - 1)
print(n)
