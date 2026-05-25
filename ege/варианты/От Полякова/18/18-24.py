from re import *
with open("24-337.txt") as f:
    s = f.read()
p = "[1-9ABCD][0-9ABCD]*[07]0"
lmax = ""
for l in finditer(p, s):
    r = l.group()
    if len(r) > len(lmax):
        lmax = r
print(len(lmax))