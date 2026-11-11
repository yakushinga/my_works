def f(n, flag15, flag7):
    if n == 25 and flag15 and not(flag7):
        return 1
    if n >= 25:
        return 0
    if n == 15:
        flag15 = True
    if n == 7:
        flag7 = True
    return f(n+1, flag15, flag7)+f(n+3, flag15, flag7)+f(n*2, flag15, flag7)
print(f(2, False, False))
