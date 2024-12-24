def is_perfect(n):
    if n < 1:
        return False
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total == n
a = int(input())
b = int(input())
perfect_numbers = []
for i in range(a, b + 1):
    if is_perfect(i):
        perfect_numbers.append(i)
print("Các số hoàn hảo trong đoạn ({}, {}): {}".format(a, b, perfect_numbers))
