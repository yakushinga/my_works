with open("17_25356.txt") as f:
    c = list(map(int, f.read().split()))
maxn = -100001
for el in c:
    if abs(el)%100 == 30 and el > maxn:
        maxn = el

ans = []
for i in range(len(c)-3):
    k = 0
    for j in range(i, i+3):
        if abs(c[j]) >= 1000 and abs(c[j]) < 10000:
            k += 1
    if k == 0 and sum(c[i:i+3]) > maxn:
        ans.append(sum(c[i:i+3]))
print(len(ans), max(ans))