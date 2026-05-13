def f(n, f53, f36):
    if n == 12 and f53 and not(f36):
        return 1
    if n <= 12:
        return 0
    if n == 53:
        f53 = True
    if n == 36:
        f36 = True
    return f(n-3, f53, f36) + f(n-6, f53, f36) + f(n//2, f53, f36)
print(f(86, False, False))