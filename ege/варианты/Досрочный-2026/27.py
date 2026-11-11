def dist(p, p0):
    return ((p[0]-p0[0])**2+(p[1]-p0[1])**2)**0.5

def clno(p):
    if p[1] > 10:
        return 1
    return 0

cl = [[] for i in range(2)]

with open("27_A_28766.txt") as f:
    for s in f:
        p = s.replace(",", ".").split()
        p[0] = float(p[0])
        p[1] = float(p[1])
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
            ci = p
    c.append(ci)
t = [el for cl0 in cl for el in cl0 if el[2][0] == "Y" and el[2][2:] == "III"]
j = 0
for i in range(1, len(cl)):
    if len(cl[i]) < len(cl[j]):
        j = i

A1 = 10**10
A2 = 0
for p in t:
    d = dist(p, c[j])
    A1 = min(A1, d)
    A2 = max(A2, d)
A1 = int(A1*10000)
A2 = int(A2*10000)
print(A1, A2)

def clno(p):
    if p[1] > 22:
        return 2
    if p[1] > 16:
        return 1
    return 0

cl = [[] for i in range(3)]

with open("27_B_28766.txt") as f:
    for s in f:
        p = s.replace(",", ".").split()
        p[0] = float(p[0])
        p[1] = float(p[1])
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
            ci = p
    c.append(ci)
zs = []

for cl0 in cl:
    zs0 = []
    for p in cl0:
        if p[2][0] == "Z" and p[2][2:] == "I":
            zs0.append(p)
    zs.append(zs0)
B1 = 10**10
for cl0 in zs:
    for p in cl0:
        for p0 in cl0:
            if dist(p, p0) != 0:
                B1 = min(B1, dist(p, p0))
B2 = dist(c[0], c[1])
B1 = int(B1*10000)
B2 = int(B2*10000)
print(B1, B2)