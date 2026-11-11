k = 0
for n in range(700000, 900000):
    p = []
    i = 2
    while i*i <= n:
        if n%i == 0:
            if i%10 == 7 and i != 7:
                p.append(i)
            if n//i%10 == 7 and n//i != 7:
                p.append(n//i)
        i += 1
    if len(p) != 0:
        print(n, min(p))
        k += 1
    if k == 5:
        break