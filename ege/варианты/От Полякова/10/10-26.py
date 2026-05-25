with open("26-155.txt") as f:
    n = int(f.readline())
    s = f.readline()
    c = []
    while s != "":
        c.append(list(map(int, s.split())))
        s = f.readline()
c = sorted(c, key=lambda x: (-x[0], -x[2], x[1]))
sumk = c[0]
maxsum = [0, 0, 0]
for i in range(1, n):
    if c[i][0] == sumk[0] and c[i][2] == sumk[2]:
        sumk[1] += c[i][1]
    else:
        if sumk[1] > maxsum[1]:
            maxsum = sumk
        sumk = c[i]
print(maxsum)