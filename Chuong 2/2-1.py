a = float(input())
b = float(input())

if a == 0:
    if b == 0:
        print("VSN")
    else:
        print("VN")
else:
    x = -b / a
    print("x = {}".format(x))
