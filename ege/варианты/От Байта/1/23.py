def f(n, flag8, flag5):
    if n == 13 and not(flag8) and flag5:
        return 1
    if n >= 13:
        return 0
    if n == 8:
        flag8 = True
    if n == 5:
        flag5 = True
    return f(n+1, flag8, flag5) + f(n+3, flag8, flag5) + f(n*2, flag8, flag5)
print(f(2, False, False))