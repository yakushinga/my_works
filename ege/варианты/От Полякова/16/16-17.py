with open("17-418.txt") as f:
    c = list(map(int, f.read().split()))
m1 = 10001
m2 = 0
for n in c:
    if n >= 1000 and n < 10000 and n < m1:
        m1 = n
    if n >= 10 and n < 100 and n > m2:
        m2 = n
o11 = m1%11
o3 = m2%3
ans = []
for i in range(len(c)-1):
    k1 = 0
    k2 = 0
    for j in range(i, i + 2):
        if c[j]%7 == o11:
            k1 += 1
        if c[j]%5 == o3:
            k2 += 1
    if k1 > 0 and k2 > 0:
        ans.append(sum(c[i:i+2]))
print(len(ans), max(ans))