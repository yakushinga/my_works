k = 0
for n in range(1350050, 2000000):
    i = 2
    p = []
    while i*i <= n:
        if n%i == 0:
            if i % 100 == 11 and i != 11:
                p.append(i)
            if n//i % 100 == 11 and n//i != 11:
                p.append(n//i)
        i += 1
    if len(p) > 0:
        minp = min(p)
        print(n, minp)
        k += 1
    if k == 5:
        break