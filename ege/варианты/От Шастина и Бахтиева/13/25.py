def S(n):
    i = 2
    k = n
    p = []
    h = 0
    while i < n:
        if k % i == 0:
            h += 1
            p.append(i)
            while k % i == 0:
                k//=i
        i += 1
    if len(p) > 0:
        return p
    return [0]
k = 0
for n in range(6700001, 7000000):
    s = S(n)
    if sum(s) > 0 and sum(s) % 2 == 0  and sum(s)%len(s)==0:
        print(n, sum(s))
        k += 1
    if k == 5:
        break
