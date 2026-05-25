with open("17_20342.txt") as f:
    c = list(map(int, f.read().split()))
maxn = -100001
for el in c:
    if abs(el) >= 10000 and abs(el) < 100000 and abs(el)%100 == 42 and el > maxn:
        maxn = el
        print(maxn)
ans = []
for i in range(len(c) - 1):
    sumkv = 0
    k = 0
    for j in range(i, i + 2):
        if abs(c[j]) >= 10000 and abs(c[j]) < 100000 and abs(c[j])%100 == 42:
            k += 1
        sumkv += c[j]*c[j]
    if k == 1 and sumkv >= maxn**2:
        ans.append(sum(c[i:i+2]))
print(len(ans), max(ans))