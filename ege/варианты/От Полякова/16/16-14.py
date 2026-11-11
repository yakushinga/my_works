def f(n):
    a = []
    while n:
        a += [n%4]
        n//=4
    return a.count(0)
ans = [0, 0]
for x in range(3001):
    if f(x) > ans[0]:
        ans = [f(x), x]
print(ans)