def dist(p0, p1):
    return ((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2)**0.5
def clnoa(p):
    if p[0] > 4:
        return 0
    return 1
cla = [[] for i in range(2)]
with open("27-76a.txt") as f:
    for s in f:
        p = list(map(float, s.replace(",",".").split()))
        cla[clnoa(p)].append(p)
r = []
for cl in cla:
    minsumdist = 10**10
    for p in cl:
        sumdist = 0
        for p0 in cl:
            sumdist += dist(p, p0)
        if sumdist < minsumdist:
            cent = p
            minsumdist = sumdist
    maxdist = 0
    for p0 in cl:
        maxdist = max(maxdist, dist(cent, p0))
    r.append(maxdist)
sr = int(sum(r)/len(r)*10000)
print(sr)
def clnoa(p):
    if p[1] > p[0] + 1:
        if p[1] > -p[0] + 9:
            return 3
        return 1
    if p[1] > -p[0] + 9:
        return 2
    return 0
cla = [[] for i in range(4)]
with open("27-76b.txt") as f:
    for s in f:
        p = list(map(float, s.replace(",",".").split()))
        cla[clnoa(p)].append(p)
r = []
for cl in cla:
    minsumdist = 10**10
    for p in cl:
        sumdist = 0
        for p0 in cl:
            sumdist += dist(p, p0)
        if sumdist < minsumdist:
            cent = p
            minsumdist = sumdist
    maxdist = 0
    for p0 in cl:
        maxdist = max(maxdist, dist(cent, p0))
    r.append(maxdist)
sr = int(sum(r)/len(r)*10000)
print(sr)