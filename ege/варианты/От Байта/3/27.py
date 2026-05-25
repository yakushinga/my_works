def dist(p1, p0):
    return ((p1[1]-p0[1])**2+(p1[0]-p0[0])**2)**0.5
def clno(p):
    if p[1] > 18:
        return 1
    return 0
cl = [[] for i in range(2)]
with open("27_A_24871.txt") as f:
    for s in f:
        p = list(map(float, s.replace(",",".").split()))
        cl[clno(p)].append(p)
c = []
for cl0 in cl:
    minsd = 10**10
    for p0 in cl0:
        sd = 0
        for p1 in cl0:
            sd += dist(p0, p1)
        if sd < minsd:
            minsd = sd
            c0 = p0
    c.append(c0)
Px = -100
Py = -100
for p in c:
    Px = max(Px, p[0])
    Py = max(Py, p[1])
Px = abs(int(Px*10000))
Py = abs(int(Py*10000))
print(Px, Py)

def clno(p):
    if p[1] > 98:
        return 2
    if p[1] > 62:
        return 1
    return 0
cl = [[] for i in range(3)]
with open("27_B_24871.txt") as f:
    for s in f:
        p = list(map(float, s.replace(",",".").split()))
        cl[clno(p)].append(p)
c = []
for cl0 in cl:
    minsd = 10**10
    for p0 in cl0:
        sd = 0
        for p1 in cl0:
            sd += dist(p0, p1)
        if sd < minsd:
            minsd = sd
            c0 = p0
    c.append(c0)
maxp = 0
minp = 0
for i in range(1, len(cl)):
    if len(cl[i]) > len(cl[maxp]):
        maxp = i
    if len(cl[i]) < len(cl[minp]):
        minp = i
Qx = int(abs(c[maxp][0]-c[minp][0])*10000)
Qy = int(abs(c[maxp][1]-c[minp][1])*10000)
print(Qx, Qy)
