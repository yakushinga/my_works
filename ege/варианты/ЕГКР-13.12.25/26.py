with open("26_25363.txt") as f:
    n = int(f.readline())
    t = []
    for l in f:
        ti = list(map(int, l.split()))
        t.append(ti)
tmin = 0
for i in range(1, n):
    if min(t[i]) > min(t[tmin]):
        tmin = i
print(tmin + 1)
d = t[tmin][1]
k = 0
for el in t:
    if el[1] == min(el) and el[1] < d:
        k += 1
print(k)
