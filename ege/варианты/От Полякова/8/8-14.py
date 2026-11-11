def f(n):
    a = []
    while n:
        a.append(n%81)
        n//=81
    k = 0
    print(a)
    for i in a:
        if i == 4:
            k += 1
    return k
print(f(77*81**2031+23*729**1037-7*9**3023))