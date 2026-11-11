def f(n, flag):
    if n < 4:
        return 0
    if n == 4 and flag:
        return 1
    if n == 66:
        flag = True
    return f(n-2, flag) + f(n//2, flag) + f(n//3, flag)
print(f(150, False))
