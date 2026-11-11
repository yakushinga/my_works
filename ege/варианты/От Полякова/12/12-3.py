from math import *
def f(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%3) + s
        n//=3
    return s

for n in range(1000):
    s = f(n)
    if n%3 == 0:
        s = s + s[-2:]
    else:
        s = s + f(3*(n%3))
    r = int(s, 3)
    if r <= 150:
        print(n)
