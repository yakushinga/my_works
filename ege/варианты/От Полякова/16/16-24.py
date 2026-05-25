from re import *
with open("24-345.txt") as f:
    s = f.read()
p = "[1-9AB][0-9AB]*[13579B]"
xmax = [0, 0]
for l in finditer(p, s):
    x = int(l.group(), 12)
    if x > xmax[0]:
        xmax = [x, l.span()[0]]
print(xmax)