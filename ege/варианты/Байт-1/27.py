def dist(p, p0):
    return ((p[0]-p0[0])**2+(p[1]-p0[1])**2)**0.5
def clno(p):
    if p[0] > 20:
        return 1
    return 0
cl = [[] for i in range(2)]
with open("27_A_23978.txt") as f:
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
            minsumdist = sumdist
            c0 = p
    c.append(c0)
Px = 10**10
Py = 10**10
for p in c:
    Px = min(Px, p[0])
    Py = min(Py, p[1])
Px = int(Px*10000)
Py = int(Py*10000)
print(Px, Py)

def clno(p):
    if p[0] < 13 and p[1] < 15:
        return 0
    if p[1] < 29 and p[1] > 21 and p[0] > 26 and p[0] < 34:
        return 1
    if p[0] > 47 and p[0] < 53 and p[1] > 36 and p[1] < 44:
        return 2
    return -1
cl = [[] for i in range(3)]
with open("27_B_23978.txt") as f:
    for s in f:
        p = list(map(float, s.replace(",", ".").split()))
        if clno(p) != -1:
            cl[clno(p)].append(p)
c = []
for cl0 in cl:
    minsumdist = 10**10
    for p in cl0:
        sumdist = 0
        for p0 in cl0:
            sumdist += dist(p, p0)
        if sumdist < minsumdist:
            minsumdist = sumdist
            c0 = p
    c.append(c0)
Q2 = 0
for i in range(3):
    for p in cl[i]:
        Q2 = max(Q2, dist(p, c[i]))

minp = 0
maxp = 0
for i in range(1, 3):
    if len(cl[i]) < len(cl[minp]):
        minp = i
    if len(cl[i]) > len(cl[maxp]):
        maxp = i

Q1 = dist(c[minp], c[maxp])
Q1 = int(Q1*10000)
Q2 = int(Q2*10000)
print(Q1, Q2)
