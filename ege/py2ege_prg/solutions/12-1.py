with open ("/home/user/repo/ege/py2ege_prg/12/data/data12-1.txt") as f:
    c = f.read().split()
for i in range(len(c)):
    c[i] = int(c[i])
max3 = -10000
for i in range(len(c)):
    if abs(c[i])%10 == 3 and c[i] >= max3:
        max3 = c[i]

k = 0
maxs = 0

for i in range(len(c)-2):
    sumkv = 0
    k3 = 0
    for j in range(i, i+2):
        if abs(c[j])%10 == 3:
            k3 += 1
        sumkv += c[j]**2
    if sumkv >= max3**2 and k3 == 1:
        k += 1
        maxs = max(sumkv, maxs)
print(k, maxs)