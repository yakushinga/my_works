def sumdel(n):
    r = 1 + n
    i = 2
    while i*i <= n:
        if n%i == 0:
            r += i
            if i*i < n:
                r += n//i
        i += 1
    return r
k  = 0
for n in range(500001, 600000):
    r = sumdel(n)
    if r%10 == 6:
        print(n, r)
        k += 1
    if k == 5:
        break