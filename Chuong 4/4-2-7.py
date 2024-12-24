s = input()
x = input()
count = 0
for c in s:
    if c == x:
        count +=1
print("So lan xuat hien cua '{}': {}".format(x,count))