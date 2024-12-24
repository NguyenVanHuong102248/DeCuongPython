s = input()
hoa = 0
thuong = 0
so = 0
for c in s:
    if c.isupper():
        hoa += 1
    elif c.islower():
        thuong += 1
    elif c.isdigit():
        so += 1
print("So chu cai viet hoa: {}".format(hoa))
print("So chu cai viet thuong: {}".format(thuong))
print("So chu so: {}".format(so))

