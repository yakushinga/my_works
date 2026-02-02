with open("26-177.txt") as f:
    k = int(f.readline())
    m = []
    for i in range(k):
        n, nd, nk, = f.readline().split()
        n, nd, nk = int(n), int(nd), int(nk)
        m.append((n, nd, nk))
m.sort(key = lambda x: x[1])
print(m)
n = 1
maxc1 = 1
maxc2 = 1
c1 = 1
c2 = 1
minn = m[0][0]
minn0 = m[0][0]
for i in range(1, k):
    if m[i][1] == m[i-1][1]:
        if m[i][1]//25 - m[i-1][1]//25 == 1:
            c1 += 1
        c2 += 1
        minn0 = min(m[i][0], minn0)