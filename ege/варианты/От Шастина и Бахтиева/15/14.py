def f(n):
    k = 0
    while n:
        cif = n % 7
        if cif % 2 == 1:
            k += 1
        n//=7
    return k
maxk = 0
for x in range(1, 1001):
    k = f(7**270+7**170+7**70-x)
    if k >= maxk:
        maxk = k
        maxx = x
print(maxx)