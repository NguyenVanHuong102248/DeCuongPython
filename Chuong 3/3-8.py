def doi(n):
    binary = ""
    while n > 0:
        x = n % 2
        binary = str(x) + binary
        n //= 2
    return binary

n = int(input())
print("Dạng nhị phân của {} là: {}".format(n, doi(n)))
