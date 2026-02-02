def dist(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

cla = [[] for i in range(2)]

def nocla(x, y):
    if y > 0:
        return 1
    return 0

for s in open("27-95a.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    k = nocla(x, y)
    cla[k].append((x, y))

centers = []
for cl in cla:
    minsumdist = 10000*100
    for p0 in cl:
        sumdist = 0
        for p in cl:
            sumdist += dist(p, p0)
        if sumdist < minsumdist:
            minsumdist = sumdist
            center = p0
    centers.append(center)
px = 0
py = 0
for x in centers:
    px += x[0]
    py += x[1]
px /= 2
py /= 2
print(int(px*10000), int(py*10000))

def noclb(x, y):
    if x < 0:
        return 1
    if y > 0:
        return 2
    return 0

clb = [[] for i in range(3)]

for s in open("27-95b.txt"):
    x, y = s.replace(',','.').split()
    x, y = float(x), float(y)
    k = noclb(x, y)
    clb[k].append((x, y))

centers = []
for cl in clb:
    minsumdist = 10000*100
    for p0 in cl:
        sumdist = 0
        for p in cl:
            sumdist += dist(p, p0)
        if sumdist < minsumdist:
            minsumdist = sumdist
            center = p0
    centers.append(center)
px = 0
py = 0
for x in centers:
    px += x[0]
    py += x[1]
px /= 3
py /= 3
print(int(px*10000), int(py*10000))