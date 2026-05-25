def f(n, f13, f15):
    if n == 35:
        return 0
    if n == 51 and f13 and f15:
        return 1
    if n == 51:
        return 0
    if n > 51:
        return 0
    if n == 13:
        f13 = True
    if n == 15:
        f15 = True
    return f(n+1,f13,f15) + f(n+2,f13,f15) + f(n*2,f13,f15)
print(f(7, False, False))