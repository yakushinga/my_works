with open("17_29842.txt") as f:
    c = list(map(int, f.read().split()))

s = 0
for el in c:
    if abs(el) >= 10000 and abs(el) < 100000 and abs(el) % 2 == 0:
        s += el

s = abs(s)%10

ans = []
for i in range(len(c)- 1):
    k = 0
    for j in range(i, i + 2):
        if abs(c[j]) % 10 == s:
            k += 1
    if k == 1:
        ans.append(abs(c[i]-c[i+1]))
print(len(ans), max(ans))