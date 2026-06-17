def dist(p, p0):
    return ((p[0]-p0[0])**2 + (p[1]-p0[1])**2)**0.5

def clno(p):
    if p[0] > 0:
        return 0
    return 1

cl = [[] for i in range(2)]
with open("27A_30475.txt") as f:
    for s in f:
        p = s.split()
        p[0] = float(p[0])
        p[1] = float(p[1])
        cl[clno(p)].append(p)

c = []
for cl0 in cl:
    mind = 10**10
    for p0 in cl0:
        d = 0
        for p in cl0:
            d += dist(p, p0)
        if d < mind:
            ci = p0
            mind = d
    c.append(ci)
maxp = 0
if len(cl[1]) > len(cl[0]):
    maxp = 1

cls = cl[0] + cl[1]
A = []
mind = 10**10
for p in cls:
    d = dist(c[maxp], p)
    if p[2][0] == "O" and p[2][2:] == "V" and d < mind:
        mind = d
        A = p
Ax = int(A[0]*10000)
Ay = int(A[1]*10000)

print(Ax, Ay)

def clno(p):
    if p[1] > 0:
        return 2
    if p[0] > 0:
        return 1
    return 0

cl = [[] for i in range(3)]
with open("27B_30475.txt") as f:
    for s in f:
        p = s.split()
        p[0] = float(p[0])
        p[1] = float(p[1])
        cl[clno(p)].append(p)

c = []
for cl0 in cl:
    mind = 10**10
    for p0 in cl0:
        d = 0
        for p in cl0:
            d += dist(p, p0)
        if d < mind:
            ci = p0
            mind = d
    c.append(ci)

maxp = 0
minp = 0
k = [0]*3
for i in range(3):
    for p in cl[i]:
        if p[2][2:] == "IV":
            k[i] += 1

for i in range(1, 3):
    if k[i] > k[maxp]:
        maxp = i
    if k[i] < k[minp]:
        minp = i

B1 = int(10000*dist(c[maxp], c[minp]))

bsvg = [[] for i in range(3)]

for i in range(3):
    for p in cl[i]:
        if p[2][0] == "A" and p[2][2:] == "I":
            bsvg[i].append(p)

B2 = 0
for cl in bsvg:
    for p in cl:
        for p0 in cl:
            B2 = max(B2, dist(p, p0))

B2 = int(10000*B2)

print(B1, B2)