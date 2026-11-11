def prime(m):
    i = 2
    while i*i <= m:
        if m%i == 0:
            return False
        i += 1
    return True
def M(n):
    i = 2
    p = []
    while i*i <= n:
        if n%i == 0:
            if prime(i):
                p.append(i)
            if prime(n//i):
                p.append(n//i)
        i += 1
    if len(p) == 0:
        return 0
    return max(p) + min(p)
ans = []
k = 0
for n in range(23600000, 24000000):
    m = M(n)
    if m%213 == 171:
        ans.append([n, m])
        k += 1
    if k == 6:
        break
print(*ans)