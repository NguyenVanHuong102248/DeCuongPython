s = input()
count = {}
for c in s:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1
for c in count:
    print("'{}': {}".format(c,count[c]))
        