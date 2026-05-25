with open("26-156.txt") as f:
    n = int(f.readline())
    q = list(map(int, f.readline().split()))
    u = []
    s = f.readline()
    while s != "":
        s = list(map(int, s.split(" ")))
        ni = s[0]
        si = 0
        hi = 0
        ki = 0
        for i in range(1, 11):
            si += q[i-1]*s[i]
            if s[i] < 0:
                hi += q[i-1]
            if s[i] == 0:
                ki += 1
        u.append([si, hi, ki, ni])
        s = f.readline()

u = sorted(u, key = lambda x: (-x[0], x[1], x[2], x[3]))

for i in range(n//5, n):
    if u[i][0] != u[i-1][0] or u[i][1] != u[i-1][1] or u[i][2] != u[i-1][2]:
        j = i
        break
for i in range(n):
    if u[i][0] <= 0:
        l = i
        break
print(u[j], u[j-1])
print(u[l], u[l-1])

s = 0
for i in range(j, j + (l-j)//10):
    s += u[i][0]
print(s)