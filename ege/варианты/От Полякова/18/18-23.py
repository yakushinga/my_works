def f(n, flag):
    if n == 1 and flag:
        return 1
    if n <= 1:
        return 0
    if n == 8:
        flag = True
    return f(n-1, flag) + f(n//2, flag)
print(f(30, False))