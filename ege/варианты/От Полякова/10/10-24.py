from re import *

with open("24-347.txt") as f:
    s = f.read()
p = "[123456789AB][0123456789AB]*"
smax = ["", 0]
for i in finditer(p, s):

    j = i.span()[-1] - 1
    r = i.group()
    if int(r, 12)%3 == 0:
        if len(r) > len(smax[0]):
            smax = [r, j]
        elif len(r) == len(smax[0]) and int(r, 12) < int(smax[0], 12):
            smax = [r, j]
print(smax)
s = "123gdfAB"
for i in finditer(p, s):
    print(i)