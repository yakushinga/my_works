k = 0
for n in range(300000, 400000):
    p = 0
    i = 2
    while i*i <= n:
        if n%i == 0:
            if i%2 == 1:
                p += i
            if n//i%2 == 1:
                p += n//i
        i += 1
    if p % 10 == 7:
        print(n, p)
        k += 1
    if k == 5:
        break
