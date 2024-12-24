s = input()
a = ' '.join(s.split())
b = ' '.join(c.capitalize() for c in a.split())
print(b) 