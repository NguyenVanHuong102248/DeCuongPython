def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
n = int(input())
num = []
for i in range(1, n + 1):
    num.append(fibonacci(i))
print("Các số Fibonacci từ F(1) đến F({}): {}".format(n, num))
print("Tổng các số Fibonacci:", sum(num))
