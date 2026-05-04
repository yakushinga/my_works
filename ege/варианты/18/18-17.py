with open("17-418.txt") as f:
    c = list(map(int, f.read().split()))
o1 = min(c)%5
o2 = max(c)%7
ans = []
for i in range(len(c)-1):
    k1 = 0
    k2 = 0
    for j in range(i, i+2):
        if c[j]%5 == o1:
            k1 += 1
        if c[j]%7 == o2:
            k2 += 1
    if k1 > 0 and k2 > 0:
        ans.append(sum(c[i:i+2]))
print(len(ans), max(ans))