with open ("17-426.txt") as f:
    c = list(map(int, f.read().split()))
c2 = max(c)%10
c1 = max(c, key=abs)%10

a = []
for i in range(len(c)-3):
    k1 = 0
    k2 = 0
    k3 = 0
    for j in range (i, i+3):
        if abs(c[j]) >= 1000 and abs(c[j]) < 10000:
            k1 += 1
        if abs(c[j])%10 == c1:
            k2 += 1
        if abs(c[j])%10 == c2:
            k3 += 1
    if k1 > 0 and k2 <= 1 and k3 >= 1:
        a.append(sum(c[i:i+3]))
print(len(a), sum(a)//len(a))