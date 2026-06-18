with open("26_30082.txt") as f:
    N = int(f.readline())
    flag = False
    r = []
    for i in range(N):
        k = list(map(int, f.readline().split()))
        if not(flag):
            flag = True
            id = k[0]
            ball = k[4]
        if k != []:
            r.append([k[4], k[1]/k[2], k[3], k[0]])
v = []
sr = 0
for el in r:
    sr += el[0]
sr/=len(r)

for el in r:
    if el[0] > sr:
        v.append(el)

v.sort(key = lambda x: (-x[1], -x[2], x[3]))

k = 0
for i in range(len(v)):
    if v[i][3] == id:
        m = i + 1
        break
    if v[i][0] < ball:
        k += 1
print(m, k)
