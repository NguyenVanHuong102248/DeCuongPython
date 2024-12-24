def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a = int(input())
b = int(input())
print("UCLN của {} và {} là: {}".format(a, b, gcd(a, b)))
