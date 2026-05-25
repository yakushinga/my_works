def dist(p, p0):
    return ((p[0]-p0[0])**2 + (p[1]-p0[1])**2)**0.5
def clnoa(p):
    if p[1] > -p[0] + 8:
        return 1
    return 0
cla = [[] for i in range(2)]
with open("27-78a.txt") as f:
    s = f.readline().replace(",", ".")
    while s != "":
        p = list(map(float, s.split()))
        cla[clnoa(p)].append(p)
        s = f.readline().replace(",", ".")
dA = []
for cl in cla:
    c = [10**12, [0,0]]
    for p in cl:
        sumdist = 0
        for p0 in cl:
            sumdist += dist(p, p0)
        if sumdist < c[0]:
            c = [sumdist, p]
    d = 0
    for p0 in cl:
        d = max(d, dist(c[1], p0))
    dA.append(d)
print(int(sum(dA)/len(dA)*10000))

def clnob(p):
    if p[1] > -p[0] + 12:
        if p[1] > p[0] - 3:
            return 3
        return 1
    if p[1] > p[0] - 3:
        return 2
    return 0
clb = [[] for i in range(4)]
with open("27-78b.txt") as f:
    s = f.readline().replace(",", ".")
    while s != "":
        p = list(map(float, s.split()))
        clb[clnob(p)].append(p)
        s = f.readline().replace(",", ".")
dB = []
for cl in clb:
    c = [10**12, [0,0]]
    for p in cl:
        sumdist = 0
        for p0 in cl:
            sumdist += dist(p, p0)
        if sumdist < c[0]:
            c = [sumdist, p]
    d = 0
    for p0 in cl:
        d = max(d, dist(c[1], p0))
    dB.append(d)
print(int(sum(dB)/len(dB)*10000))