from operator import ifloordiv

with open("26-159.txt") as f:
    n = int(f.readline())
    a = []
    for b in range (n):
        s = f.readline()
        i, k = s.split()
        i, k = int(i), int(k)
        a.append((i, k))
a.sort()

b = a
a = []
for i in range(1, len(b)):
    if b[i] != b[i-1]:
        a.append(b[i])
n = len(a)

print(a)
i = 1
maxn = [a[0][0],1]
while i < n:
    num = a[i][0]
    i += 1
    k = 1
    while i < n and a[i][0] == num and i < n:
        k1 = 1
        while i < n and a[i][1] == a[i-1][1] + 1 and a[i][0] == num:
            k1 += 1
            i += 1
        i += 1
        k = max(k1, k)
    if k > maxn[1]:
        maxn = [num, k]
print(maxn)