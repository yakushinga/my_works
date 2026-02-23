from math import *
m = []

def f1(n):
    buf = n
    k = 0
    while buf:
        if buf % 10 == 2:
            k += 1
        buf //= 10
    if k == 1:
        return True
    return False

def f(n):
    i = 2
    flag1 = True
    while i * i <= n and flag1:
        if n % i == 0:
            flag1 = False
        i += 1
    if flag1:
        return f1(n)
    return False

for n in range(2, int(sqrt(9000000))):
    if f(n):
        m.append(n)
m.sort()
print(m)
k1 = 0
for k in range(6651220, 7000000):
    n = k
    for i in range(len(m)):
        if n%m[i] == 0:
            n//=m[i]
            break
    if k!=n and f(n) and k1 < 5:
        k1 += 1
        print(k , n)