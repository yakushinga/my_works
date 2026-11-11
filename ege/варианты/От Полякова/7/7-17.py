with open ("17-428.txt") as f:
    c = list(map(int, f.read().split()))
min7 = abs(min(c))%7
min5 = abs(max(c))%5
k = 0
ssum = 0
for i in range(len(c)-2):
    k1 = 0
    k2 = 0
    k3 = 0
    for j in range(i, i+3):
        if abs(c[j]) >= 100 and abs(c[j])<1000:
            k1 += 1
        if abs(c[j])%5 == min7:
            k2 += 1
        if abs(c[j])%7 == min5:
            k3 += 1
    if k1 > 0 and k2 <= 1 and k3 >= 2:
        k += 1
        ssum += sum(c[i:i+3])
print(k, ssum//k)