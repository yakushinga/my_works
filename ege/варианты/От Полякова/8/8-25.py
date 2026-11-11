from math import *
def f(n):
    if str(n).count("5") != 1:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True
p = []
for n in range(2, int(3000000//2)):
    if f(n):
        p.append(n)
print(p)
k = 0
for n in range(1324728, 3000000):
    flag = False
    for m in p:
        if n%m == 0:
            flag = f(n//m)
            l = n//m
            break
    if flag:
        print(n, l)
        k += 1
    if k == 5:
        break