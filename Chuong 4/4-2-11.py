import re
s = input()
a = re.findall(r'-?\d+',s)
print(max(a))
