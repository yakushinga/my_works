with open("26-156.txt") as f:
    n = int(f.readline())
    q = list(map(int, f.readline().split()))
    s = list(map(int, f.readline().split()))
    u = []
    while len(s) > 0:
        summ = 0
        shtr = 0
        prop = 0
        for i in range(1, 11):
            summ += s[i]*q[i-1]
            if s[i] == -1:
                shtr += q[i-1]
            if s[i] == 0:
                prop += 1
        u.append([summ, shtr, prop, s[0]])
        s = list(map(int, f.readline().split()))
u = sorted(u, key=lambda x: (-x[0], x[1], x[2], x[3]))
k = 0
for i in range(n):
    if u[i][0] == u[1199][0] and u[i][1] == u[1199][1] and u[i][2] == u[1199][2]:
        k += 1
for i in range(n//3, n):
    if u[i][0] != u[i-1][0] or u[i][1] != u[i-1][1] or u[i][2] != u[i-1][2]:
        j = i
        break
print(u[j], k)