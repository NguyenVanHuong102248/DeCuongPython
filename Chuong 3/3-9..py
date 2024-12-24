def doi16(n):
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        term = n % 16
        hexadecimal = hex_digits[term] + hexadecimal
        n //= 16
    return hexadecimal

n = int(input())
print("Dạng thập lục phân của {} là: {}".format(n, doi16(n)))
