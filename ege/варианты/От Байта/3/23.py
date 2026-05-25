from sys import *
setrecursionlimit(50000)
def f(n, f10, f20):
    if n == 30 and f10 + f20 == 1:
        return 1
    if n >= 30:
        return 0
    if n == 10:
        f10 = 1
    if n == 20:
        f20 = 1
    return f(n+1, f10, f20) + f(n+5, f10, f20) + f(n*5, f10, f20)
print(f(1, 0, 0))