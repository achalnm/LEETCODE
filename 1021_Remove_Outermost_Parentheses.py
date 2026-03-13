s = "(()())(())"

result = []
depth = 0
for c in s:
    if c == "(":
        if depth > 0:
            result.append(c)
        depth = depth + 1
        
    else:
        depth = depth -1
        if depth > 0:
            result.append(c)

p = "".join(result)
print(p)
            