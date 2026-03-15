with open("26-191.txt") as f:
    n, k = list(map(int, f.readline().split()))
    a = list(map(int, f.read().split()))
a.sort(reverse=True)
s = 6*a[0]**2
v = a[0]**3
prev = a[0]
for i in range(1, len(a)):
    if prev - a[i] >= k:
        prev = a[i]
        s += 4*a[i]**2
        v += a[i]**3
print(v, s)