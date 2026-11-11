from re import *
with open("24-347.txt") as f:
    s = f.read()
p = "[1-9AB][0-9AB]*[0369]"
smax = [0, 0]
for l in finditer(p, s):
    n = int(l.group(), 12)
    if n > smax[0]:
        smax = [n, l.span()[0]]
print(smax)