with open("26-156.txt") as f:
    n = int(f.readline())
    q = list(map(int, f.readline().split()))
    s = f.readline()
    u = []
    while s != "":
        a = list(map(int, s.split()))
        kp = 0
        sh = 0
        summ = 0
        for i in range(1, 11):
            summ += q[i-1]*a[i]
            if a[i] == 0:
                kp += 1
            if a[i] < 0:
                sh += q[i-1]
        u.append([summ, sh, kp, a[0]])
        s = f.readline()
u = sorted(u, key= lambda x: (-x[0], x[1], x[2], x[3]))
u1000 = u[999]
for i in range(n//4, n):
    if u[i][0] != u[i-1][0] or u[i][1] != u[i-1][1] or u[i][2] != u[i-1][2]:
        j = i
        break
k = 0
for m in u:
    if u1000[0] == m[0] and u1000[1] == m[1] and u1000[2] == m[2]:
        k += 1
print(u[j][3], k)