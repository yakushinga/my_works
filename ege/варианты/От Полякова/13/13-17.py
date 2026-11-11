with open("17-418.txt") as f:
    c = list(map(int, f.read().split()))
o11 = max(c)%11
o3 = min(c)%3
ans = []
for i in range(len(c)-3):
    k1 = 0
    k2 = 0
    for j in range(i, i+3):
        if c[j]%3 == o11:
            k1 += 1
        if c[j]%11 == o3:
            k2 += 1
    if k1 == 1 and k2 == 1:
        ans.append(sum(c[i:i+3]))
print(len(ans), min(ans))
