import math

x = float(input())
ep = float(input())
S = 1
n = 1
term = x

while term >= ep:
    S += term
    n += 1
    term = x**n / math.factorial(n)

print("Giá trị gần đúng của e^x:", S)
