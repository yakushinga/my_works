def dist(p, p0):
    return ((p[0]-p0[0])**2+(p[1]-p0[1])**2)**0.5
def clnoa(p):
    if p[0] > 2:
        if p[1] > 2:
            return 2
        return 3
    if p[1] > 0:
        return 0
    return 1
cla = [[] for i in range(4)]
with open("27-80a.txt") as f:
    s = f.readline().replace(",", ".")
    while s != "":
        p = list(map(float, s.split()))
        s = f.readline().replace(",", ".")
        cla[clnoa(p)].append(p)

s = []
for cl in cla:
    d = []
    for i in range(len(cl)):
        for j in range(i + 1, len(cl)):
            d += [dist(cl[i], cl[j])]
    s.append(sum(d)/len(d))
print(int(min(s)*100000), int(max(s)*100000))
def clnob(p):
    if p[0] > 6:
        if p[1] > 3:
            return 1
        return 0
    if p[0] > 1:
        if p[1] > 1:
            return 3
        return 2
    if p[0] > -4:
        if p[1] > -3:
            return 5
        return 4
    return 6
clb = [[] for i in range(7)]
with open("27-80b.txt") as f:
    s = f.readline().replace(",", ".")
    while s != "":
        p = list(map(float, s.split()))
        s = f.readline().replace(",", ".")
        clb[clnob(p)].append(p)

s = []
for cl in clb:
    d = []
    for i in range(len(cl)):
        for j in range(i + 1, len(cl)):
            d += [dist(cl[i], cl[j])]
    s.append(sum(d)/len(d))
print(int(min(s)*100000), int(max(s)*100000))