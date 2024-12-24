import math

a, b, c = map(float, input().split())
if a == 0:
    if b ==0:
        if c == 0:
            print("VSN")
        else:
            print("VN")
    else:
        print("{:.3f}".format(-c/b))        
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("VN")
    elif delta == 0:
        x = -b / (2*a)
        print("{:.3f}".format(x))
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("{:.3f} {:.3f}".format(x1, x2))
