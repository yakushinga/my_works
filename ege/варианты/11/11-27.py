def dist(p, p0):
    return ((p[0]-p0[0])**2 + (p[1]-p0[1])**2)**0.5

def clnoA(p):
    if p[0] > 2:
        if p[1] > 2:
            return 3
        return 1
    if p[1] > 0:
        return 2
    return 0

clA = [[] for i in range(4)]
with open("27-82a.txt") as f:
    s = f.readline()
    while s != "":
        p = list(map(float, s.replace(",", ".").split(" ")))
        clA[clnoA(p)].append(p)
        s = f.readline()

izA = []
for cl in clA:
    k  = 0
    kmin = [100000000, [0,0]]
    for p in cl:
        for p0 in cl:
            if dist(p, p0) <= 1:
                k += 1
        if k < kmin[0]:
            kmin = [k, p]
    izA.append(kmin[1])
print(izA)

def clnoB(p):
    if p[0] > 6:
        if p[1] > 2:
            return 6
        return 1
    if p[0] > 1:
        if p[1] > 1:
            return 5
        return 2
    if p[0] >= -4:
        if p[1] > -2:
            return 3
        return 0
    return 4

clB = [[] for i in range(7)]
with open("27-82b.txt") as f:
    s = f.readline()
    while s != "":
        p = list(map(float, s.replace(",", ".").split(" ")))
        clB[clnoB(p)].append(p)
        s = f.readline()

izB = []
for cl in clB:
    k  = 0
    kmin = [100000000, [0,0]]
    for p in cl:
        for p0 in cl:
            if dist(p, p0) <= 1:
                k += 1
        if k < kmin[0]:
            kmin = [k, p]
    izB.append(kmin[1])
print(izB)

sx = 0
sy = 0
for p in izA:
    sx += p[0]
    sy += p[1]
px = int(abs(sx/len(izA)*100000))
py = int(abs(sy/len(izA)*100000))
print(px, py)

sx = 0
sy = 0
for p in izB:
    sx += p[0]
    sy += p[1]
px = int(abs(sx/len(izB)*100000))
py = int(abs(sy/len(izB)*100000))
print(px, py)
