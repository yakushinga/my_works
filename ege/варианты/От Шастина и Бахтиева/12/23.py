from math import *

def f(n, f30, f15):
    if n == 7 and not(f30) and f15:
        return 1
    if n <= 7:
        return 0
    if n == 30:
        f30 = True
    if n == 15:
        f15 = True
    return f(n-1, f30, f15) + f(n-3, f30, f15) + f(ceil(n/2), f30, f15)
print(f(35, False, False))