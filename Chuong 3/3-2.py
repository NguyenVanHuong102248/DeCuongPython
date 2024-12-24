def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
primes = []
for i in range(1, n + 1):
    if is_prime(i):
        primes.append(i)
print("Các số nguyên tố trong khoảng (1, {}): {}".format(n, primes))
