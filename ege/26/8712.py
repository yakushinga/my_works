with open("26-181.txt") as f:
    k = int(f.readline())
    s = f.readline()
    m = []
    while s != "":
        n, t1, t2 = s.split(' ')
        t1, t2 = int(t1), int(t2)
        m.append((t1, t2))
        s = f.readline()
summ = 0
maxx = 0
for i in range(k):
    maxx = max(m[i][1], maxx)
print(maxx)
a = [0]*(maxx + 1)

for i in range(len(m)):
    for j in range (m[i][0]+1, m[i][1]+1):
        a[j] += 1

i = 0
n = 0

while i <= len(a) - 1:
    if a[i] == 2:
        n += 1
        summ += 1
        i += 1
        while a[i] == 2 and i <= len(a)-1:
            summ += 1
            i += 1
    i += 1
print(n, summ)