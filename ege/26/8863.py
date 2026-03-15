# R - 1 G - 2 B - 3
a = [[] for i in range(3)]
with open ("26-192.txt") as f:
    n = int(f.readline())
    s = f.readline()
    color = {"R":0, "G":1, "B": 2}
    while s != "":
        k = s.split()
        k[-1] = color[k[-1]]
        k = list(map(int, k))
        a[k[-1]].append([k[1], k[0]])
        s = f.readline()
a[0].sort(reverse=True)
a[1].sort(reverse=True)
a[2].sort(reverse=True)
b = [[] for i in range(3)]
for i in range(3):
    while len(a[i]) > 0:
        bi  = [a[i][0]]
        p = [0]
        for j in range(1, len(a[i])):
            if bi[-1][0] - a[i][j][0] >= 2:
                bi += [a[i][j]]
                p.append(j)
        for j in range(len(p)-1, -1, -1):
            a[i].pop(p[j])
        b[i].append(bi)
sr = 0
for m in b[0][0]:
    sr += m[0]
sb = 0
for m in b[2][0]:
    sb += m[0]
print(sr - sb, len(b[1]))