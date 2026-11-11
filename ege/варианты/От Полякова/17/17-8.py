from heapq import nlargest


def f(n):
    a = []
    while n:
        a.append(n%14)
        n//=14
    k1 = 0
    k2 = 0
    for i in a:
        if i == 9:
            k1  += 1
        if i > 10:
            k2 += 1
    return k1 == 1 and k2 <= 3
k = 0
for n in range(14**4, 14**5):
    if f(n):
        k += 1
print(k)
