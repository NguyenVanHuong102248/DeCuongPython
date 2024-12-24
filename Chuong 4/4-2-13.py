t = int(input())
for _ in range(t):
    s = input()
    count = {}
    a = []
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
            a.append(c)
    result = ""
    for c in a:
        result += "{}{}".format(c, count[c])
    print(result)
