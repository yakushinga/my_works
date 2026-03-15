with open("26-190.txt") as f:
    n = int(f.readline())
    s = f.readline()
    a = []
    while s != "":
        s = list(map(int, s.split()))
        a.append([s[-1], s[0]])
        s = f.readline()
a.sort(reverse=True)
b = []
while len(a) > 0:
    bi = [a[0]]
    p = [0]
    for j in range(1, len(a)):
        if bi[-1][0] - a[j][0] >= 3:
            bi.append(a[j])
            p.append(j)
    for i in range(len(p)-1, -1, -1):
        a.pop(i)
    if len(bi) >= 2:
        b.append(bi)
print(b)