k = 0
for n in range(1000000, 2000000):
    q = 0
    i = 2
    while i*i <= n:
        if n%i == 0:
            q += i
            if i*i != n:
                q += n//i
        i += 1
    flag = True
    j = 2
    while j*j <= q and flag:
        if q % j == 0:
            flag = False
        j += 1
    if flag and q != 0:
        print(n, q)
        k += 1
    if k == 5:
        break
