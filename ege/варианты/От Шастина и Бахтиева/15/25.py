from fnmatch import fnmatch
def f(n):
    i = 2
    os = []
    while i*i <= n:
        if n % i == 0:
            if fnmatch(str(i), "?3*"):
                os.append(i)
            if fnmatch(str(n//i), "?3*"):
                os.append(n//i)
        i += 1
    return os

k = 0
for n in range(1000501, 1100000):
    os = f(n)
    if len(os) >= 14:
        print(n, sum(os))
        k += 1
    if k == 5:
        break