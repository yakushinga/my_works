def prost(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def f(n):
    i = 2
    d = []
    while i*i <= n:
        if n % i == 0:
            d.append(i)
            if i*i < n:
                d.append(n//i)
        i += 1
    if len(d) < 20:
        return 0
    pr = []
    for el in d:
        if el <= 100:
            continue
        else:
            if prost(el):
                pr.append(el)
    if len(pr) < 2:
        return 0
    else:
        return max(pr)

k = 0
for n in range(3000000, 4000000):
    maxd = f(n)
    if maxd != 0:
        print(n, maxd)
        k += 1
    if k == 4:
        break