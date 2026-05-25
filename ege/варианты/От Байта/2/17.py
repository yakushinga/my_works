with open ("17_24235.txt") as f:
    c = list(map(int, f.read().split()))
maxn = 0
for el in c:
    if abs(el) >= 1000 and abs(el) < 10000:
        maxn = max(maxn, el)

ans = []
for i in range(len(c)-1):
    k = 0
    for j in range(i, i + 2):
        if abs(c[j]) >= 1000 and abs(c[j]) < 10000:
            k += 1
    if k == 1 and abs(c[i]*c[i+1])%maxn == 0:
        ans.append(c[i]*c[i+1])
print(len(ans), abs(min(ans)))