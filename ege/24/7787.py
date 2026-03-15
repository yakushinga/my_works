from re import (finditer)
with open("24-306.txt") as f:
    s = f.read()
p = "AFD(0|[1-9][0-9]*)([+*](0|[1-9][0-9]*))+"
smax = ""
for i in finditer(p, s):
    s = i.group()
    if len(s) > len(smax):
        smax = s
print(len(smax))