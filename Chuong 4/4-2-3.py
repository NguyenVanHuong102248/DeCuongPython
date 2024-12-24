s = input()
c = input()

result = ""
for ch in s:
    if ch != c:
        result += ch
print(result)