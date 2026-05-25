def f(n, flag):
    if n == 3 and flag:
        return 1
    if n <= 3:
        return 0
    if n == 18:
        flag = True
    return f(n - 2, flag) + f(n//2 , flag) + f(n//3, flag)
print(f(50, False))