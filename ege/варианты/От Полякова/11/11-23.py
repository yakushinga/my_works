def f(n):
    if n == 18:
        return 0
    if n == 3:
        return 1
    if n < 3:
        return 0
    f1 = f(n-2)
    if n%2 == 0:
        f2 = f(n//2)
    else:
        f2 = f(n-3)
    return f1 + f2
print(f(55))