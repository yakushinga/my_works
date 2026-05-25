def dist(p, p0):
    return ((p[0]-p0[0])**2+(p[1]-p0[1])**2)**0.5
def clnoA(p):
    if p[1] > 5:
        return 1
    return 0
clA = [[] for i in range(2)]
with open ("27-84a.txt") as f:
    s = f.readline()
    while s != "":
        p = list(map(float, s.replace(',', '.').split()))
        clA[clnoA(p)].append(p)
        s = f.readline()
dA = []
for i in range(2):
    cl = clA[i]
    diag = [clA[i][0], clA[i][1], 0]
    for p in cl:
        for p0 in cl:
            dist0 = dist(p, p0)
            if dist0 > diag[2]:
                diag = [p, p0, dist0]
    dA.append(diag)

Px = (dA[0][0][0] + dA[0][1][0] + dA[1][0][0] + dA[1][1][0])/4*10000
Py = (dA[0][0][1] + dA[0][1][1] + dA[1][0][1] + dA[1][1][1])/4*10000
print(int(Px), int(Py))

def clnoB(p):
    if p[0] > 6:
        return 1
    if p[1] > 6:
        return 2
    return 0

clB = [[] for i in range(3)]
with open ("27-84b.txt") as f:
    s = f.readline()
    while s != "":
        p = list(map(float, s.replace(',', '.').split()))
        clB[clnoB(p)].append(p)
        s = f.readline()
dA = []

for i in range(3):
    cl = clB[i]
    diag = [clB[i][0], clB[i][1], 0]
    for p in cl:
        for p0 in cl:
            dist0 = dist(p, p0)
            if dist0 > diag[2]:
                diag = [p, p0, dist0]
    dA.append(diag)

Px = (dA[0][0][0] + dA[0][1][0] + dA[1][0][0] + dA[1][1][0]+ dA[2][0][0] + dA[2][1][0])/6*10000
Py = (dA[0][0][1] + dA[0][1][1] + dA[1][0][1] + dA[1][1][1]+ dA[2][0][1] + dA[2][1][1])/6*10000
print(int(Px), int(Py))