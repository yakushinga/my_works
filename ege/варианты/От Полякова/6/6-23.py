def f(n, f1, f2):
    if n == 56:
        return 0
    if n == 89 and f1 and f2:
        return 1
    if n >= 89:
        return 0
    if n == 40:
        f1 = True
    if n == 72:
        f2 = True
    print(n)
    return f(n + 3, f1, f2) + f(n + 7, f1, f2) + f(n * 3, f1, f2)
print(f(12, False, False))