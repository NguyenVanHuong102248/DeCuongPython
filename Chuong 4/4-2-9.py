s = input()
num = s.split(',')
kq = []
for i in num:
    if int(i) % 2 != 0:
        kq.append(i)
print(", ".join(kq))