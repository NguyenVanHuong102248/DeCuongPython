a = float(input())
b = float(input())

if a == 0:
    if b > 0:
        print("Bất phương trình đúng với mọi x.")
    else:
        print("Bất phương trình vô nghiệm.")
else:
    x = -b / a
    if a > 0:
        print("Nghiệm x > {}".format(x))
    else:
        print("Nghiệm x < {}".format(x))
