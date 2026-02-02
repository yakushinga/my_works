with open("26-181.txt") as f:
    k = int(f.readline())
    s = f.readline()
    m = []
    while s != "":
        n, t1, t2 = s.split(' ')
        n, t1, t2 = int(n), int(t1), int(t2)
        m.append((n, t1, t2))
        s = f.readline()
m.sort(key = lambda x: x[1])

count = 1
flag = 0
maxsumm = 0
nach = m[0][1]
maxgr = m[0][2]
for i in range(1,k):
    if m[i][1] <= maxgr:
        maxgr = max(m[i][2], maxgr)
    else:
        count += 1
        maxsumm = max(maxsumm, maxgr - nach)
        nach = m[i][1]
        maxgr = m[i][2]
print(k,count, maxsumm)