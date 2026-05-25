def dist(p, p0):
    return ((p[0]-p0[0])**2 + (p[1]-p0[1])**2)**0.5

def clno(p):
    if p[0] > 1:
        return 1
    if p[1] > 0:
        return 2
    return 0

cl = [[] for i in range(3)]
with open("27_A_22169.txt") as f:
    for s in f:
        p = list(map(float, s.replace(",", ".").split()))
        cl[clno(p)].append(p)
bub = []
for cl0 in cl:
    sx = 0
    sy = 0
    for p in cl0:
        sx += p[0]
        sy += p[1]
    x = sx/len(cl0)
    y = sy/len(cl0)
    bub.append([x, y])

px = 0
py = 0
for p in bub:
    px += p[0]
    py += p[1]
px = px/len(bub)
py = py/len(bub)
px = int(px*10000)
py = int(py*10000)
print(px, py)

def clno(p):
    if p[0] < -1.5:
        if p[1] > 0:
            return 2
        return 1
    if p[1] > p[0] - 1:
        return 3
    if p[1] > -p[0] + 1:
        return 4
    return 0

cl = [[] for i in range(5)]
with open("27_B_22169.txt") as f:
    for s in f:
        p = list(map(float, s.replace(",", ".").split()))
        cl[clno(p)].append(p)
bub = []
for cl0 in cl:
    sx = 0
    sy = 0
    for p in cl0:
        sx += p[0]
        sy += p[1]
    x = sx/len(cl0)
    y = sy/len(cl0)
    bub.append([x, y])

px = 0
py = 0
for p in bub:
    px += p[0]
    py += p[1]
px = px/len(bub)
py = py/len(bub)
px = int(px*10000)
py = int(py*10000)
print(px, py)