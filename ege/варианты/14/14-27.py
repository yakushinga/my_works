def dist(p, p0):
    return ((p[0]-p0[0])**2+(p[1]-p0[1])**2)**0.5
def clnoa(p):
    if p[0] > 2:
        if p[1] > 2:
            return 3
        return 1
    if p[1] > 0:
        return 2
    return 0
cla = [[] for i in range(4)]
with open("27-79a.txt") as f:
    s = f.readline().replace(",", ".")
    while s!= "":
        p = list(map(float, s.split()))
        cla[clnoa(p)].append(p)
        s = f.readline().replace(",", ".")
d = []
for cl in cla:
    dmax = 0
    for p in cl:
        for p0 in cl:
            dmax = max(dmax, dist(p, p0))
    d.append(dmax)
print(int(min(d)*100000), int(sum(d)/len(d)*100000))

def clnob(p):
    if p[0] < -4:
        return 0
    if p[0] < 1:
        if p[1] > -3:
            return 1
        return 2
    if p[0] < 6:
        if p[1] > 1:
            return 3
        return 4
    if p[1] > 2:
        return 5
    return 6

clb = [[] for i in range(7)]
with open("27-79b.txt") as f:
    s = f.readline().replace(",", ".")
    while s!= "":
        p = list(map(float, s.split()))
        clb[clnob(p)].append(p)
        s = f.readline().replace(",", ".")
d = []
for cl in clb:
    dmax = 0
    for p in cl:
        for p0 in cl:
            dmax = max(dmax, dist(p, p0))
    d.append(dmax)
print(int(min(d)*100000), int(sum(d)/len(d)*100000))