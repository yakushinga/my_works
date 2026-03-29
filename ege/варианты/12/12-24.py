from re import *
with open("24-347.txt") as f:
    s = f.read()
p = '[123456789AB]+[0123456789AB]*'
imax = [0, 0]
for i in finditer(p, s):
    n = int(i.group(), 12)
    if n%6 == 0 and n > imax[0]:
        imax = [n, i.span()[-1]-1]
print(imax)
