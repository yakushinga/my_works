# R - 1 G - 2 B - 3
a = [[] for i in range(3)]
with open ("26-192.txt") as f:
    n = int(f.readline())
    s = f.readline()
    color = {"R":0, "G":1, "B": 2}
    while s != "":
        k = s.split()
        k[-1] = color[k[-1]]
        k = list(map(int, k))
        a[k[-1]].append([k[1], k[0]])
        s = f.readline()
a[0].sort(reverse=True)
a[1].sort(reverse=True)
a[2].sort(reverse=True)
b = []
while len(a[0]) and len(a[1]) and len(a[2]):
    bi = [a[0][0]]
    i = 0
    while a[0][0][0] - a[1][0][0] < 2:
        a[1].pop(0)
    bi += [a[1][0]]
    while a[1][0][0] - a[2][0][0] < 2:
        a[2].pop(0)
    bi += [a[2][0]]
    a[1].pop(0)
    a[2].pop(0)
    b.append(bi)
    a[0].pop(0)
    print(bi)
print(len(b), b[-1][1][1])