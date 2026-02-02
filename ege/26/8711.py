with open("26-181.txt") as f:
    k = int(f.readline())
    s = f.readline()
    m = []
    while s != "":
        n, t1, t2 = s.split(' ')
        t1, t2 = int(t1), int(t2)
        m.append((t1, t2))
        s = f.readline()
m.sort()
maxgr = m[0][1]
n = 2
summ = m[0][0] + 365*24*60*60 - m[k-1][1]
for i in range(1, k):
    if m[i][0] <= maxgr:
        maxgr = max(maxgr, m[i][1])
    else:
        n += 1
        summ += m[i][0] - maxgr
        maxgr = m[i][1]
print(n, summ)
