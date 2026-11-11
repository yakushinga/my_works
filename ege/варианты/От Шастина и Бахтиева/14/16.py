from sys import *
setrecursionlimit(100000)

def g(n):
    if n < 221440:
        return -3 + g(n+13)
    return 52 + n/60

def f(n):
    if n > 56:
        return 1790 + f(n-5)
    return 6*(g(n-7)-31)
print(f(1614))