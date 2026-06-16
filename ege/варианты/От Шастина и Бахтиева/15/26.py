with open("26_30581.txt") as f:
    n, m = map(int, f.readline().split())
    d = []
    for i in range(m):
        t, num, type = f.readline().split()
        t, num = int(t), int(num)
        d.append([t, num, type])

d.sort(key = lambda x: (x[0], x[1], -ord(x[2])))
correct = [0]*(n + 1)
cond = [0]*(n + 1)
for s in d:
    if s[2] == "A":
        if cond[s[1]] == 0:
            correct[s[1]] += 1
            cond[s[1]] = 1
    else:
        if cond[s[1]] == 1:
            correct[s[1]] += 1
            cond[s[1]] = 0

maxcor = 0
for i in range(n, -1, -1):
    if correct[i] > maxcor:
        maxcor = correct[i]
        j = i
print(sum(correct), j)