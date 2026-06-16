
def f(n, m0, m1, m2):
    if n == 50 and m0 and not(m1) and not(m2):
        return 1
    if n >= 50:
        return 0
    if n == 21:
        m0 = True
    if n == 26:
        m1 = True
    if n == 40:
        m2 = True
    return f(n+2, m0, m1, m2) + f(n+5, m0, m1, m2) + f(n*2, m0, m1, m2)
print(f(11, False, False, False))