from re import *
with open('24_24240.txt') as f:
    s = f.read()
lmax = 0
for c in "0123456789":
    p = c + "[A-Z]*" + c
    for l in finditer(p, s):
        dl = len(l.group())
        if dl > lmax:
            lmax = dl
            i = l.start()
print(lmax, i)