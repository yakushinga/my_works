def dist(p, p0):
    return ((p[0]-p0[0])**2+(p[1]-p0[1])**2)**0.5

def clno(p):
    if p[1] > 3:
        return 1
    return 0

cl = [[] for i in range(2)]
with open("27A_29941.txt") as f:
    for s in f:
        p = list(map(float, s.split()))
        cl[clno(p)].append(p)

per = []

for cl0 in cl:
    minn = 10**5
    for p0 in cl0:
        n = 0
        for p1 in cl0:
            if dist(p0, p1) <= 1:
                n += 1
        if n < minn:
            minn = n
            pi = p0
    per.append(pi)

Px = 0
Py = 0

for p in per:
    Px += p[0]
    Py += p[1]

Px = int(10000*(Px/2))
Py = int(10000*(Py/2))

print(Px, Py)

def clno(p):
    if p[0] > 12:
        return 0
    if p[1] < 4:
        return 1
    if p[1] < 10:
        return 2
    if p[1] < 14:
        return 3
    return 4

cl = [[] for i in range(5)]
with open("27B_29941.txt") as f:
    for s in f:
        p = list(map(float, s.split()))
        cl[clno(p)].append(p)

per = []
Q1 = 0
for cl0 in cl:
    minn = 10**5
    for p0 in cl0:
        n = 0
        for p1 in cl0:
            if dist(p0, p1) <= 1:
                n += 1
        if n < minn:
            minn = n
            pi = p0
    Q1 = max(Q1, minn)
    per.append(pi)

Q2 = 0

for p0 in per:
    for p1 in per:
        Q2 = max(Q2, dist(p0, p1))

Q2 = int(Q2*10000)

print(Q1, Q2)