from sys import *
setrecursionlimit(100000)
def g(n):
    if n >= 248045:
        return n/20 + 28
    return g(n + 9) - 4
def f(n):
    if n >= 19:
        return f(n-4) + 3580
    return 6*(g(n-7)-36)
print(f(673))