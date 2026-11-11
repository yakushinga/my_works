from re import *
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
with open ("24_29923.txt") as f:
    s = f.read()

p = "([BCDFGHJKLMNPQRSTVWXZ][02468][13579][AEIOUY])+"

lmax = 0
for l in finditer(p, s):
    lmax = max(lmax, len(l.group()))

print(lmax//4)
