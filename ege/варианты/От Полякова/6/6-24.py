with open ("24-347.txt") as f:
    c = f.read()
alf = "0123456789AB"
n = len(c)
i = 0
p = []

while i < n:
    if c[i] != '0' and c[i] in alf:
        p0 = [i]
        s = ""
        while c[i] in alf and i < n:
            s += c[i]
            i += 1
        p0.append(int(s,12))
        p0.append(i-1)
        if (p0[1]%9 == 0):
            p.append(p0)
    i += 1

maxp = p[0]
for i in range(1, len(p)):
    if p[i][2] - p[i][0] + 1 > maxp[2] - maxp[0] + 1:
        maxp = p[i]
    elif p[i][2] - p[i][0] + 1 == maxp[2] - maxp[0] + 1 and p[i][1] < maxp[1]:
        maxp = p[i]
print(maxp[2])