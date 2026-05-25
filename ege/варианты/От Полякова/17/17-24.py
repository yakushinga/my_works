from re import *
with open("24-337.txt") as f:
    s = f.read()
p = "[1][0-9ABCD]*[07]"
maxlen = 0
for l in finditer(p, s):
    print(l.group())
    maxlen = max(maxlen, len(l.group()))
print(maxlen)