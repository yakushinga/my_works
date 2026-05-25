with open("17_23970.txt") as f:
    c = list(map(int, f.read().split()))
maxel = 0
for el in c:
    if el >= 100 and el < 1000 and el > maxel:
        maxel = el
ans = []
for i in range(len(c)-1):
    k = 0
    for j in range(i, i+2):
        if c[j] >= 100 and c[j] < 1000:
            k += 1
    if k == 1 and c[i]*c[i+1]%maxel == 0:
        ans.append(c[i]*c[i+1])
print(len(ans), min(ans))