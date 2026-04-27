from math import *
resh = [1]*10000000
prime = []
for i in range(2, 10000000//2):
    if resh[i] == 1:
        prime.append(i)
        for j in range(i*2, 10000000, i):
            resh[j] = 0

def F(n):
    a = []
    for p in prime:
        if n % p == 0:
            a.append(p)
        if p >= n:
            break

    if len(a) == 0:
        return 0
    return int(sum(a)/len(a))
k = 0
ans = []
for n in range(9500000, 10000000):
    f = F(n)
    if f != 0 and f%813 == 0:
        ans.append((n, f))
        k += 1
    if k == 5:
        break
    print(n)
ans.sort(key=lambda x: (x[1], x[0]))
print(ans)