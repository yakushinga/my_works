def prime(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

def d(n):
    i = 2
    ans = []
    while i*i <= n:
        if n%i == 0:
            if i%1000 == 777 and prime(i):
                ans.append(i)
            if (n//i)%1000 == 777 and prime(n//i):
                ans.append(n//i)
        i += 1
    if len(ans) > 0:
        return min(ans)
    return 0
k = 0
ans = []
for n in range(55000000, 56000000):
    l = d(n)
    if l > 0:
        ans.append([n, l])
        k += 1
    if k == 4:
        break
ans.sort(key = lambda x: (x[1], x[0]))
print(*ans)