from math import *
def f(n):
    k8 = 0
    k10 = 0
    while n:
        c = n%15
        if c == 8:
            k8 += 1
        if c > 9:
            k10 += 1
        n//=15
    return k8 == 1 and k10 >= 2
k = 0
for n in range(15**4, 15**5):
    if f(n):
        k += 1
print(k)
print(bin(128)[2:])