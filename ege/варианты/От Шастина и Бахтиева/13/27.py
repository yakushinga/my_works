def dist(p0, p1):
    return ((p0[0]-p1[0])**2+(p0[1]-p1[1])**2)**0.5
def clno(p):
    if p[1] > 12:
        return 1
    return 0

cl = [[] for i in range(2)]
with open("27A_29942.txt") as f:
    for s in f:
        p = list(map(float, s.split()))
        cl[clno(p)].append(p)

antic = []
for cl0 in cl:
    maxd = 0
    for p0 in cl0:
        d = 0
        for p in cl0:
            d += dist(p0, p)
        if d > maxd:
            maxd = d
            ac = p0
    antic.append(ac)

P1 = int(10000*(dist(antic[1], [0, 0])))
P2 = int(10000*((dist(antic[0], [1.1, -3.3]) + dist(antic[1], [1.1, -3.3]))/2))

print(P1, P2)

def clno(p):
    if p[1] > 0 and p[1] < 12:
        return 0
    if p[1] > 12 and p[1] < 21:
        return 1
    if p[1] > 21 and p[1] < 26:
        return 2
    return -1

cl = [[] for i in range(3)]
with open("27B_29942.txt") as f:
    for s in f:
        p = list(map(float, s.split()))
        if clno(p) != -1:
            cl[clno(p)].append(p)

antic = []
for cl0 in cl:
    maxd = 0
    for p0 in cl0:
        d = 0
        for p in cl0:
            d += dist(p0, p)
        if d > maxd:
            maxd = d
            ac = p0
    antic.append(ac)

Q1 = 0
Q2 = 0
for c0 in antic:
    for c in antic:
        Q1 = max(Q1, dist(c, c0))
    Q2 += dist(c0, [-4.4, 2.2])
Q1 = int(10000*Q1)
Q2 = int(10000*Q2)
print(Q1, Q2)