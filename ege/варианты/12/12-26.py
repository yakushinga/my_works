with open ("26-153.txt") as f:
    n = int(f.readline())
    t = []
    s = f.readline()
    while s != "":
        ti = list(map(int, s.split()))
        t.append(ti)
        s = f.readline()
t.sort(key = lambda x: (x[1], x[2], x[0]))
sr = sum(item[1] for item in t)/len(t)
d = []
for item in t:
    if item[1] > sr:
        d.append(item)
lider = [0, 0, 0, 0]
if d[0][2] == 0:
    li = [d[0][0], d[0][1], 1, 0]
else:
    li = [d[0][0], d[0][1], 0, 1]

for i in range(1, len(d)):
    if li[0] == d[i][0]:
        if d[i][2] == 0:
            li[2] += 1
        else:
            li[3] += 1
    else:
        if li[2] > lider[2]:
            lider = li
        elif li[2] == lider[2] and li[1] > lider[1]:
            lider = li
        elif li[2] == lider[2] and li[1] == lider[1] and li[3] < lider[3]:
            lider = li
        
        if d[i][2] == 0:
            li = [d[i][0], d[i][1], 1, 0]
        else:
            li = [d[i][0], d[i][1], 0, 1]
print(lider)
k = 0
for m in d:
    if m[0] == 45510 and m[2] == 1:
        k += 1
print(k*lider[1])
