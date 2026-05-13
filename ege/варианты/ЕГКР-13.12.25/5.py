from math import log


from math import *
def f(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%3) + s
        n//=3
    return s
rmin = 10000
for n in range(9, 1000):
    s = f(n)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        sumcif = sum(map(int, s))
        s = s + f(sumcif*3)
    r = int(s, 3)
    if r%2 == 1 and r < rmin and r > 208:
        rmin = r
print(rmin, f(rmin))
print(log(16384, 2))