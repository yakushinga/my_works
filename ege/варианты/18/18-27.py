def dist(p,p1):
    return ((p[0]-p1[0])**2+(p[1]-p1[1])**2)**0.5
def clno(p):
    if p[1] > 3:
        return 1
    return 0
cl = [[] for i in range(2)]
with open("27-75a.txt") as f:
    for s in f:
        p = list(map(float, s.replace(",", ".").split()))
        cl[clno(p)].append(p)
r = []
for cl0 in cl:
    mindist = 10**10
    for p in cl0:
        sumdist = 0
        for p0 in cl0:
            sumdist += dist(p, p0)
        if sumdist < mindist:
            c = p
            mindist = sumdist
    R = 0
    for p in cl0:
        R = max(R, dist(c, p))
    r.append(R)
print(int(sum(r)/len(r)*10000))

def clno(p):
    if p[1] > 0.5*p[0] + 1:
        if p[1] > -p[0] + 10:
            return 3
        return 2
    if p[0] > 6:
        return 0
    return 1
cl = [[] for i in range(4)]
with open("27-75b.txt") as f:
    for s in f:
        p = list(map(float, s.replace(",", ".").split()))
        cl[clno(p)].append(p)
r = []
for cl0 in cl:
    mindist = 10**10
    for p in cl0:
        sumdist = 0
        for p0 in cl0:
            sumdist += dist(p, p0)
        if sumdist < mindist:
            c = p
            mindist = sumdist
    R = 0
    for p in cl0:
        R = max(R, dist(c, p))
    r.append(R)
print(int(sum(r)/len(r)*10000))