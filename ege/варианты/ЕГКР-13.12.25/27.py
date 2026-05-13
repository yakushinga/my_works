def dist(p, p0):
    return ((p[0]-p0[0])**2 + (p[1]-p0[1])**2)**0.5

def clno(p):
    if p[1] > 10:
        return 1
    return 0

cl = [[] for i in range(2)]
with open("27_A_25364.txt") as f:
    for s in f:
        p = list(map(float, s.replace(",", ".").split()))
        cl[clno(p)].append(p)

c = []


for cl0 in cl:
    minsumdist = 10**10
    for p in cl0:
        sumdist = 0
        for p0 in cl0:
            sumdist += dist(p, p0)
        if minsumdist > sumdist:
            c0 = p
            minsumdist = sumdist
    c.append(c0)
d = []
for c0 in c:
    d.append(dist([1, 1], c0))
P1 = int(min(d)*10000)
P2 = int(max(d)*10000)
print(P1, P2)

def clno(p):
    if p[1] > 22:
        return 2
    if p[1] > 16:
        return 1
    return 0

cl = [[] for i in range(3)]
with open("27_B_25364.txt") as f:
    for s in f:
        p = list(map(float, s.replace(",", ".").split()))
        cl[clno(p)].append(p)

c = []

for cl0 in cl:
    minsumdist = 10**10
    for p in cl0:
        sumdist = 0
        for p0 in cl0:
            sumdist += dist(p, p0)
        if sumdist < minsumdist:
            c0 = p
            minsumdist = sumdist
    c.append(c0)

maxp = 0
if len(cl[1]) > len(cl[maxp]):
    maxp = 1
if len(cl[2]) > len(cl[maxp]):
    maxp = 2
Q1 = 0
Q2 = 0
for p0 in cl[maxp]:
    d = dist(c[maxp], p0)
    if d <= 1.2:
        Q1 += 1
    if d <= 0.75:
        Q2 += 1
print(Q1, Q2)
