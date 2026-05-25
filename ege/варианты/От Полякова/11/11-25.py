def f(n):
    i = 2
    m = 0
    while i*i <= n:
        if n%i == 0:
            m = i + n//i
            break
        i += 1
    return m
k = 0
for n in range(700000, 800000):
    m = f(n)
    if m%10 == 4:
        print(n, m)
        k += 1
    if k == 5:
        break