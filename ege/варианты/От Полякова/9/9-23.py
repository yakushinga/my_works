def f(n, f19, f29):
    if n == 24:
        return 0
    if n == 6 and f19 and f29:
        return 1
    if n <= 6:
        return 0
    if n == 19:
        f19 = True
    if n == 29:
        f29 = True
    return f(n//2, f19, f29) + f(n-1, f19, f29) + f(n-6, f19, f29)
print(f(34, False, False))