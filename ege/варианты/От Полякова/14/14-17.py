with open("17-418.txt") as f:
    c = list(map(int, f.read().split()))
o5 = min(c)%5
o7 = max(c)%7
ans = []
for i in range(len(c)-3):
    k1 = 0
    k2 = 0
    for j in range(i, i+3):
        if c[j]%5 == o5:
            k1 += 1
        if c[j]%7 == o7:
            k2 += 1
    if k1 == 1 and k2 == 1:
       ans += [sum(c[i:i+3])]
print(len(ans), min(ans))