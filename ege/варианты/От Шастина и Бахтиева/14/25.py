def f(n):
    i = 2
    k = 0
    maxi = 0
    m = n
    while i <= m and k <= 3:
        if n % i == 0:
            if str(i).count("2") != 1:
                return 0
            k += 1
            maxi = max(i, maxi)
            n//=i
            while n % i == 0:
                k += 1
                n//=i
        i += 1
    if k == 3 and n == 1:
        return maxi
    return 0

k = 0
for n in range(5000000, 6000000):
    maxi = f(n)
    if maxi != 0:
        print(n, maxi)
        k += 1
    if k == 5:
        break