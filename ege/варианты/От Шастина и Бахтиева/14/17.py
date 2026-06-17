with open("17_29841.txt") as f:
    c = list(map(int, f.read().split()))

min17 = 100001
for el in c:
    if el > 0 and el % 17 == 0 and el < min17:
        min17 = el
ans = []
for i in range(len(c) - 1):
    if c[i] != c[i+1] and abs(c[i]-c[i+1])%min17 == 0:
        ans.append(c[i]*c[i+1])
print(len(ans), max(ans))