from sys import *
setrecursionlimit(1000000)

def f(n):
    if n < 1110:
        return n
    return (n-5)*f(n-7)
print((f(1223526)-f(1223519))/(6*f(1223512)))