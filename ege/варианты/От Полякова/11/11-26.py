with open("26-154.txt") as f:
    n = int(f.readline())
    zd = []
    nzd = []
    for i in range(n):
        s = f.readline()
        s = list(map(int, s.split()))
        if s[1:5].count(2) == 0:
            sr = sum(s[1:5])/4
            zd.append([s[0], sr])
        else:
            k = s[1:5].count(2)
            nzd.append([s[0], k])
zd.sort(key = lambda x: (-x[1], x[0]))
nzd.sort(key = lambda x: (x[1], x[0]))
print(zd)
print(nzd)
print(zd[n//4-1])
for i in range(len(nzd)):
    if nzd[i][1] == 3:
        print(nzd[i])
        break