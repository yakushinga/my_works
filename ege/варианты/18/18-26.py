with open("26-142.txt") as f:
    n = int(f.readline())
    t = []
    for s in f:
        t.append(list(map(int, s.split())))
t.sort()
p = []
time = 0
i = 0
while i < len(t):
    mintime = t[i][1]
    mini = i
    j = i + 1
    while j < len(t) and t[j][0] < mintime + 10:
        if t[j][1] < mintime:
            mintime = t[i][1]
            mini = j
        j += 1
    p.append(t[mini])
    i = j

print(len(p))
print(p)