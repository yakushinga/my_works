with open("26-151.txt") as f:
    n, k = map(int, f.readline().split())
    s = f.readline()
    m = []
    while s != "":
        mi = list(map(int, s.split()))
        m.append([mi[0], sum(mi[1:4]), mi[4]])
        s = f.readline()
m.sort(key = lambda x: (-x[1], -x[2], x[0]))
print(m[k-1])
for i in range(k-2, 0, -1):
    if m[i][1] > m[k-1][1]:
        print(m[i][0])
        break
l = 0
for i in range(n):
    if m[i][1] == m[k-1][1]:
        l += 1

print(l)