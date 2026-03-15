from re import *
with open("24-300.txt") as f:
    s = f.read()
p = "(0|[1-9][0-9]*)([+*]0|[1-9][0-9]*)+"
a = findall(p, s)
print(a)