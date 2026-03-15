with open("26-186.txt") as f:
    n, k = list(map(int, f.readline().split()))
    cost = []
    for i in range(n):
        num, price = list(map(int, f.readline().split()))
        cost.append([price, num])
    t = []
    for i in range(k):
        ti = list(map(int, f.readline().split()))
        t.append(ti)
cost.sort()
t.sort()

used = []
income = {}
k = {}
for m in cost:
    income[m[1]] = 0
    k[m[1]] = 0

for day in range(1, 366):
    for i in range(len(t)):
        if t[i][0] == day:
            if len(cost) == 0:
                break
            used.append([t[i][1], cost[0]])
            income[cost[0][1]] += (t[i][1] - t[i][0]+1)*cost[0][0]
            k[cost[0][1]] += 1
            cost.pop(0)

    p = []
    for i in range(len(used)):
        if used[i][0] == day:
            cost.append(used[i][1])
            p.append(i)
    for i in range(len(p) - 1, -1, -1):
        used.pop(p[i])
    cost.sort()

print(max(income, key=income.get))
print(k[max(k, key=k.get)])