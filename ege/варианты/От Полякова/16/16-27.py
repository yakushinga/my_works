def dist(p,p0):
    return ((p[0]-p0[0])**2 + (p[1]-p0[1])**2)**0.5
def clnoa(p):
    if p[1] > p[0] - 1:
        return 1
    return 0
cla = [[]for i in range(2)]
with open("27-77a.txt") as f:
    s = f.readline().replace(",", ".")
    while s != "":
        p = list(map(float, s.split()))
        cla[clnoa(p)].append(p)
        s = f.readline().replace(",", ".")
r = []
for cl in cla:
    minp = [10000000000000, [0,0]]
    for p in cl:
        sumdist = 0
        for p0 in cl:
            sumdist += dist(p, p0)
        if sumdist < minp[0]:
            minp = [sumdist, p]
    maxd = 0
    for p in cl:
        maxd = max(dist(minp[1], p), maxd)
    r.append(maxd)
ravg = int((sum(r)/len(r))*10000)
print(ravg)

def clnob(p):
    if p[1] > p[0] + 1:
        if p[1] > -p[0] + 8:
            return 3
        return 1
    if p[1] > -p[0] + 8:
        return 2
    return 0
clb = [[]for i in range(4)]
with open("27-77b.txt") as f:
    s = f.readline().replace(",", ".")
    while s != "":
        p = list(map(float, s.split()))
        clb[clnob(p)].append(p)
        s = f.readline().replace(",", ".")
r = []
for cl in clb:
    minp = [10000000000000, [0,0]]
    for p in cl:
        sumdist = 0
        for p0 in cl:
            sumdist += dist(p, p0)
        if sumdist < minp[0]:
            minp = [sumdist, p]
    maxd = 0
    for p in cl:
        maxd = max(dist(minp[1], p), maxd)
    r.append(maxd)
ravg = int((sum(r)/len(r))*10000)
print(ravg)