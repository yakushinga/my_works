from re import *
with open("24_29921.txt") as f:
    s = f.read()
p = "([0-9]*[02468][0-9]*[+-])+([0-9]*[02468][0-9]*)"
maxl = 0
for l in finditer(p, s):
    maxl = max(maxl, len(l.group()))
print(maxl)