from re import *
with open ("24-345.txt") as f:
    s = f.read()
p = "[1-9ABCD][0-9ABCD]*[02468AC]"
lmax = [0, 0]
for l in finditer(p, s):
    n = int(l.group(), 14)
    if n > lmax[0]:
        lmax = [n, l.span()[0]]
print(lmax)