from math import *
def dist(p, p0):
    return sqrt((p[0]-p0[0])**2 + (p[1] - p0[1])**2)

def clnoA(p):
    if p[0] < 0 and p[1] > 0:
        return 2
    if p[1] < 0 and p[0] < 1:
        return 0
    if p[0] > 3 and p[1] < 2:
        return 1
    return 3

clA = [[] for i in range(4)]

with open("27-83a.txt") as f:
     s = f.readline()
     while s != "":
         p = list(map(float, s.replace(",", ".").split(" ")))
         clA[clnoA(p)].append(p)
         s = f.readline()

plA = [0]*4

for i in range(4):
    cl = clA[i]
    sumk = 0
    for p in cl:
        k = 0
        for p0 in cl:
            if dist(p, p0) <= 1:
                k += 1
        sumk += k
    plA[i] = sumk/len(clA[i])
print(int(min(plA)*100000), int(sum(plA)/len(plA)*100000))

def clnoB(p):
    if p[0] > 6:
        if p[1] > 0:
            return 6
        return 1
    if p[0] > 1:
        if p[1] > 1:
            return 5
        return 2
    if p[1] < -4:
        return 0
    if p[0] > -4:
        return 4
    return 3

clB = [[] for i in range(7)]

with open("27-83b.txt") as f:
     s = f.readline()
     while s != "":
         p = list(map(float, s.replace(",", ".").split(" ")))
         clB[clnoB(p)].append(p)
         s = f.readline()

plB = [0]*7

for i in range(7):
    cl = clB[i]
    sumk = 0
    for p in cl:
        k = 0
        for p0 in cl:
            if dist(p, p0) <= 1:
                k += 1
        sumk += k
    plB[i] = sumk/len(clB[i])
print(int(min(plB)*100000), int(sum(plB)/len(plB)*100000))