def f(n, flag):
    if flag and n == 26:
        return 1
    if n == 9:
        return 0
    if n == 14:
        flag = True
    if n > 26:
        return 0

    return f(n+1, flag) + f(n*2, flag) + f(n*3, flag)

print(f(1, False))