import re
s = input()
a = re.findall(r'-?\d+',s)
n = [int(num) for num in a]
print(sum(n))