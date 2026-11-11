def dist(p0, p1):
    return ((p0[0]-p1[0])**2+(p0[1]-p1[1])**2)**0.5

def clno(p):
    if p[1] < 0:
        return 0
    if p[0] > 0:
        return 1
    return 2

cl = [[] for i in range(3)]

with open("27A_30660.txt") as f:
    for s in f:
        p = list(s.split())
        p[0] = float(p[0])
        p[1] = float(p[1])
        cl[clno(p)].append(p)

ac = []
for cl0 in cl:
    maxd = 0
    for p in cl0:
        d = 0
        for p0 in cl0:
            d += dist(p, p0)
        if d > maxd:
            maxd = d
            antic = p
    ac.append(antic)

Ax = 0
Ay = 0
for i in range(3):
    mind = 10**10
    for p in cl[i]:
        if p[2][0] == "K" and p[2][2:] == "II":
            d = dist(ac[i], p)
            if d < mind and d != 0:
                mind = d
                oyag = p
    Ax += oyag[0]
    Ay += oyag[1]
Ax = abs(int(10000*Ax))
Ay = abs(int(10000*Ay))
print(Ax, Ay)

def clno(p):
    if p[0] < -10:
        return 0
    if p[1] < -5:
        return 1
    if p[0] < 2:
        return 2
    return 3

cl = [[] for i in range(4)]

with open("27B_30660.txt") as f:
    for s in f:
        p = list(s.split())
        p[0] = float(p[0])
        p[1] = float(p[1])
        cl[clno(p)].append(p)

ac = []
for cl0 in cl:
    maxd = 0
    for p in cl0:
        d = 0
        for p0 in cl0:
            d += dist(p, p0)
        if d > maxd:
            maxd = d
            antic = p
    ac.append(antic)


B2 = 0
for p in ac:
    for p0 in ac:
        B2 = max(B2, dist(p, p0))
B2 = int(B2*10000)

cls = cl[0] + cl[1] + cl[2] + cl[3]
kr = [[] for i in range(10)]
for p in cls:
    if p[2][0] == "M":
        kr[int(p[2][1])].append(p)
B1 = 10**10
for pdkl in kr:
    for p in pdkl:
        for p0 in pdkl:
            d = dist(p, p0)
            if d != 0:
                B1 = min(B1, d)
B1 = int(B1*10000)
print(B1, B2)