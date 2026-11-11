with open("26-150.txt") as f:
    n,m,k = map(int, f.readline().split())
    z = []
    for i in range(n):
        x, y = list(map(int, f.readline().split()))
        z.append([y,x])
z.sort()
p = [z[0]]
for i in range(1, len(z)):
    if z[i][0] != z[i-1][0]:
        p.append(z[i])
r = []
for i in range(k+1):
    r.append(m + 1)
for l in p:
    r[l[0]] = l[1]
bmax = [0, 0]
for i in range(1, k):
    if min(r[i], r[i+1]) > bmax[1]:
        bmax = [i + 1, min(r[i], r[i+1]) - 1]
print(bmax)
