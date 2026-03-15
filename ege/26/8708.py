with open("26-177.txt") as f:
    n = int(f.readline())
    z = []
    for i in range(n):
        zi = list(map(int, f.readline().split()))
        z.append(zi)
z = sorted(z, key = lambda x: (x[1], x[0], x[2]))

nmax = [0, 0, 0]
dl = 0
for i in range(n):
    if dl == 0:
        dl = 1
    elif dl > 0 and z[i][1] == z[i-1][1]:
        dl += 1
    elif dl > 0 and z[i][1] != z[i-1][1]:
        if dl > nmax[0]:
            nmax = [dl, z[i-1][0], z[i-1][1]]
        elif dl == nmax[0] and z[i-1][0] < nmax[1]:
            nmax = [dl, z[i - 1][0], z[i-1][1]]
        dl = 1
print(nmax[2])
a = []
for i in range(n):
    if z[i][1] == nmax[2]:
        a.append(z[i][2]//25 + 1)
a.sort()
print(a)