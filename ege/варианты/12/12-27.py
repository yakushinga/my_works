def dist(p, p0):
    return ((p[0]-p0[0])**2 + (p[1]-p0[1])**2)**0.5

def clNoA(p):
    if p[0] > 2:
        if p[1] > 2:
            return 3
        return 1
    if p[1] > 0:
        return 2
    return 0

clA = [[] for i in range (4)]
with open ("27-81a.txt") as f:
    s = f.readline()
    while s != "":
        p = list(map(float, s.replace(",", ".").split()))
        clA[clNoA(p)].append(p)
        s = f.readline()
nA = []
for cl in clA:
    n = [[0,0],0]
    for p in cl:
        ni = [p, 0]
        for p0 in cl:
            if dist(p, p0) <= 1:
                ni[1] += 1
        if ni[1] > n[1] or ni[1] == n[1] and ni[0][0] > n[0][0]:
            n = ni
    nA.append(n[0])
px = 0
py = 0
for p in nA:
    px += p[0]
    py += p[1]
px = int(px/4*100000)
py = int(py/4*100000)
print(px, py)

def clNoB(p):
    if p[0] > 6:
        if p[1] > 0:
            return 6
        return 1
    if p[0] > 1:
        if p[1] > 1:
            return 5
        return 2
    if p[1] < -4:
        return 0
    if p[0] > -4:
        return 3
    return 4

clB = [[] for i in range (7)]
with open ("27-81b.txt") as f:
    s = f.readline()
    while s != "":
        p = list(map(float, s.replace(",", ".").split()))
        clB[clNoB(p)].append(p)
        s = f.readline()
nB = []
for cl in clB:
    n = [[0,0],0]
    for p in cl:
        ni = [p, 0]
        for p0 in cl:
            if dist(p, p0) <= 1:
                ni[1] += 1
        if ni[1] > n[1] or ni[1] == n[1] and ni[0][0] > n[0][0]:
            n = ni
    nB.append(n[0])
px = 0
py = 0
for p in nB:
    px += p[0]
    py += p[1]
px = int(px/7*100000)
py = abs(int(py/7*100000))
print(px, py)