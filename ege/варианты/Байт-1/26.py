with open("26_23977.txt") as f:
    k = int(f.readline())
    n = int(f.readline())
    time = []
    for s in f:
        time.append(list(map(int, s.split())))
time.sort()
print(time)
stack = [0]*11
k = [0]*11
for human in time:
    for i in range(1, 11):
        if stack[i] < human[0]:
            stack[i] = 0
    for i in range(1, 11):
        if stack[i] == 0:
            stack[i] = human[1]
            k[i] += 1
            posl = i
            break
    print(stack)
print(sum(k), posl)
print(k)