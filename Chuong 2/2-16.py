import math
a, b, c= map(float, input().split())
p = (a+b+c)/2
dt = math.sqrt(p*(p-a)*(p-b)*(p-c))
if a+b>c and a+c>b and b+c>a:
    print("Dien tich {:.2f}, chu vi {:.2f}".format(dt,p*2))
else:
    print("NO")