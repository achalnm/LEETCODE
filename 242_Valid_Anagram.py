from collections import Counter
s = "cat"
t = "tca"
#sr = sorted(s) == sorted(t)
sr = Counter(s) == Counter(t)
print(sr)
