import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())
a = math.sqrt((x2-x1)**2+(y2-y1)**2)
b = math.sqrt((x3-x2)**2+(y3-y2)**2)
c = math.sqrt((x3-x1)**2+(y3-y1)**2)
p = (a+b+c)/2
dt = math.sqrt(p*(p-a)*(p-b)*(p-c))
if a+b>c and a+c>b and b+c>a:
    print("Dien tich {:.2f}, chu vi {:.2f}".format(dt,p*2))
else:
    print("NO")