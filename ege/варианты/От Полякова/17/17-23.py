def f(n, flag):
    if n == 11 and flag:
        return 1
    if n>=11:
        return 0
    if n == 7:
        flag = True
    return f(n+1, flag) + f(n+2, flag) + f(n+3, flag)
print(f(5, False))