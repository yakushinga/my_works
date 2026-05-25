def f(n, flag):
    if n == 16:
        flag = True
    if n == 2 and flag:
        return 1
    if n <= 2:
        return 0
    return f(n-2, flag) + f(n//2, flag)
print(f(38, False))