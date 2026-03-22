from re import *
with open("24-347.txt") as f:
    s = f.read()
p = "[1-7][0-7]*"
smax = ""
j = 0
for i in finditer(p, s):
    n = int(i.group(), 8)
    if len(i.group()) > len(smax) and n%2 == 0:
        smax = i.group()
        j = i.span()[0]
    elif len(i.group()) == len(smax) and int(smax, 8) > n and n%2 == 0:
        smax = i.group()
        j = i.span()[0]
print(j)