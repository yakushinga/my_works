with open ("17-428.txt") as f:
    c = list(map(int, f.read().split()))
o11 = abs(min(c))%11
o7 = max(c)%7
a = []
for i in range(len(c)-3):
    k11 = 0
    k7 = 0
    k4 = 0
    for j in range(i, i+3):
        if abs(c[j])%11 == o11:
            k11 += 1
        if abs(c[j])%7 == o7:
            k7 += 1
        if abs(c[j]) >= 1000 and abs(c[j]) < 10000:
            k4 += 1
    if k4 > 0 and k11 <= 1 and k7 >= 2:
        a.append(sum(c[i:i+3]))
print(len(a), sum(a)//len(a))