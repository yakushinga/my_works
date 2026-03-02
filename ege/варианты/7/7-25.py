from math import *
r = [1]*8000001
d = []
def prime(n):
    j = 2
    flag = True
    while j * j <= n and flag:
        if n % j == 0:
            flag = False
        j += 1
    return flag

for i in range(2, int(sqrt(8000001))):
    if r[i] == 1:
        d.append(i)
        for j in range(i, 8000001, i):
            r[j] = 0

d.sort()

k1 = 0
for n in range(5400000, 6000000):
    mi = []
    for k in range(2, int(sqrt(n))):
        if n%k == 0:
            if k in d:
                mi.append(k)
            if prime(n//k):
                mi.append(n//k)

    m = 0
    if len(mi) > 0:
        m = max(mi) + min(mi)
    if m > 60000:
        s = str(m)
        if s == s[::-1]:
            print(n, m)
            k1 += 1
        if k1 == 5:
            break