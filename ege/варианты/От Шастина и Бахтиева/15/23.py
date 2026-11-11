def f(n, f1, f2):
    if n == 40 and (f1 or f2):
        return 1
    if n  >= 40:
        return 0
    if n == 20:
        f1 = True
    if n == 31:
        f2 = True
    return f(n+1, f1, f2) + f(n+7, f1, f2) + f(n*2, f1, f2)
print(f(7, False, False))