from math import ceil
def f(n, f27, f15):
    if n == 10 and not(f27) and f15:
        return 1
    if n <= 10:
        return 0
    if n == 27:
        f27 = True
    if n == 15:
        f15 = True
    return f(n-1, f27, f15) + f(n-3, f27, f15) + f(ceil(n/2), f27, f15)
print(f(35, False, False))