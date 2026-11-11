with open("26_24870.txt") as f:
    n, k = map(int, f.readline().split())
    minN = []
    for i in range(n):
        minN.append(int(f.readline()))
    mod = []
    for i in range(k):
        mod.append(list(map(int, f.readline().split())))
mod.sort(key = lambda x: (x[1], -x[0]))
gen = []
print(minN)
maxN = 0
sumc = 0
for N in minN:
    for g in mod:
        if g[0] >= N:
            gen.append(g)
            sumc += g[1]
            maxN = max(maxN, g[0])
            break
print(sumc, maxN)
