n, k = map(int,input().split())
a = list(map(int, input().split()))
x = list(map(int, input().split()))
for i in x:
    c = False
    for j in a:
        if i == j:
            c = True
            break
    if c:
        print("YES")
    else:
        print("NO")