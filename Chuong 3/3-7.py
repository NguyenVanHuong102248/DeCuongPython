def sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

n = int(input())
print("Tổng các chữ số của {} là: {}".format(n, sum(n)))
