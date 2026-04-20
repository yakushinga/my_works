with open("26-144.txt") as f:
    n, k = map(int, f.readline().split())
    cus = []
    for i in range(n):
        cus.append(list(map(int, f.readline().split())))
num = [0]*(k+1)
stack = [[] for i in range(k+1)]
cus.sort()
bad = 0
for c in cus:
    d = []
    for i in range(1, 6):
        for j in range(len(stack[i])):
            if stack[i][j] <= c[0]:
                d.append((i, j))
    d.sort(reverse=True)
    for p in d:
        del stack[p[0]][p[1]]
    if c[2] == 0:
        flag = True
        mini = 1
        for i in range(1, 6):
            if len(stack[i]) < 5 and len(stack[i]) < len(stack[mini]):
                mini = i
        if mini == 1 and len(stack[1]) < 5 or mini > 1:
            if len(stack[mini]) == 0:
                stack[mini].append(c[0] + c[1])
            else:
                stack[mini].append(max(stack[mini]) + c[1])
            num[mini] += 1
        else:
            bad += 1
    else:
        if len(stack[c[2]]) < 5:
            if len(stack[c[2]]) == 0:
                stack[c[2]].append(c[0] + c[1])
            else:
                stack[c[2]].append(max(stack[c[2]]) + c[1])
            num[c[2]] += 1
        else:
            bad += 1
print(num[5], bad)