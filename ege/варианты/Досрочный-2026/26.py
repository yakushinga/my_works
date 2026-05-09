with open("26_17643.txt") as f:
    n = int(f.readline())
    t = []
    for s in f:
        ti = list(map(int, s.split()))
        t.append(ti)
sr = 0
for el in t:
    sr += el[1]
sr = sr/len(t)
print(sr)
d = []
for el in t:
    if el[1] > sr:
        d.append(el)
d.sort(key = lambda x: (-x[0], -x[1], x[2]))
l = []
art = d[0][0]
li = [51786, 856, 1, 0]
for i in range(1, len(d)):
    if d[i][0] == li[0]:
        if d[i][2] == 0:
            li[2] += 1
        else:
            li[3] += 1
    else:
        l.append(li)
        li = [d[i][0], d[i][1], 0, 0]
        if d[i][2] == 0:
            li[2] += 1
        else:
            li[3] += 1
l.sort(key = lambda x: (-x[2], -x[1], x[3]))
print(l[0][1]*l[0][2], l[0][3])