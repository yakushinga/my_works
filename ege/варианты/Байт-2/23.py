def f(n, flag7, flag10):
    if n == 25 and (flag7 or flag10) and not(flag7 and flag10):
        return 1
    if n >= 25:
        return 0
    if n == 7:
        flag7 = True
    if n == 10:
        flag10 = True
    return f(n+1, flag7, flag10) + f(n+2, flag7, flag10) + f(n*3, flag7, flag10)
print(f(1, False, False))