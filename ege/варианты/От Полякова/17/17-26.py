with open("26-143.txt") as f:
    n = f.readline()
    a = []
    for s in f:
        a.append(list(map(int, s.split())))
a.sort()
stack = [[] for i in range(3)]
k = [0]*3
bad = 0
for auto in a:
    p = []
    for i in range(1, 3):
        for j in range(len(stack[i])):
            if stack[i][j] <= auto[0]:
                p.append((i, j))
    p.sort(reverse=True)
    for h in p:
        del stack[h[0]][h[1]]
    if auto[2] == 0:
        if len(stack[1]) < 5 or len(stack[2]) < 5:
            zap = 1
            if len(stack[2]) < len(stack[1]):
                zap = 2
            if len(stack[zap]) == 0:
                stack[zap].append(auto[0]+auto[1])
            else:
                stack[zap].append(stack[zap][-1]+auto[1])
            k[zap] += 1
        else:
            bad += 1
    else:
        if len(stack[auto[2]]) < 5:
            zap = auto[2]
            if len(stack[zap]) == 0:
                stack[zap].append(auto[0]+auto[1])
            else:
                stack[zap].append(stack[zap][-1]+auto[1])
            k[zap] += 1
        else:
            bad += 1

print(k[1], bad)