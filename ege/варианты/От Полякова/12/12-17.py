with open ("17-418.txt") as f:
    c = list(map(int, f.read().split()))
o1 = 10000
o2 = 100
for m in c:
    if m >= 10 and m < o2:
        o2 = m
    if m >= 1000 and m < o1:
        o1 = m
o2 = o2%3
o1 = o1%11
ans = []
for i in range(len(c)-3):
    k1 = 0
    k2 = 0
    for j in range(i, i+3):
        if c[j]%7 == o1:
            k1 += 1
        if c[j]%5 == o2:
            k2 += 1
    if k1 == 1 and k2 == 1:
        ans.append(sum(c[i:i+3]))
print(len(ans), min(ans))
