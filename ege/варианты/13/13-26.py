with open("26-152.txt") as f:
    n = int(f.readline())
    s = f.readline()
    t = []
    ssum = 0
    while s != "":
        ti = list(map(int, s.split()))
        t.append(ti)
        ssum += ti[1]
        s = f.readline()
sr = ssum/len(t)
t.sort(key = lambda x : (x[1], x[0]))
for i in range(n):
    if t[i][1] > sr:
        j = i
        break
d = t[j:]

t = []
ti = [d[0][0], d[0][1], 0, 0]
if d[0][2] == 1:
    ti[3] += 1
else:
    ti[2] += 1
for i in range(1, len(d)):
    if ti[0] == d[i][0]:
        if d[i][2] == 1:
            ti[3] += 1
        else:
            ti[2] += 1
    else:
        t.append(ti)
        ti = [d[i][0], d[i][1], 0, 0]
        if d[i][2] == 1:
            ti[3] += 1
        else:
            ti[2] += 1
t.sort(key =lambda x: (x[2], x[1], -x[3], x[0]))
print(t[-1][2]*t[-1][1], t[-1][3])