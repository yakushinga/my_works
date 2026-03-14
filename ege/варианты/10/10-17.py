with open("17-426.txt") as f:
    c = list(map(int, f.read().split()))
nmax = 0
for m in c:
    if abs(m) >= 10000 and abs(m) < 100000 and abs(m)%100 == 43:
        nmax = max(nmax, m)
def summkv(a):
    r = 0
    for m in a:
        r += m*m
    return r
k1 = 0
minsummkv = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
for i in range(len(c)-3):
    k = 0
    for j in range(i, i+3):
        if abs(c[j]) >= 10000 and abs(c[j]) < 100000 and abs(c[j]) % 100 == 43:
            k += 1
    if k >= 1 and summkv(c[i:i+3]) <= nmax**2:
        minsummkv = min(summkv(c[i:i+3]), minsummkv)
        k1 += 1
print(k1, minsummkv)