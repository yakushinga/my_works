with open("26_30398.txt") as f:
    n, s = map(int, f.readline().split())
    fl = []
    for i in range(n):
        gb, type = f.readline().split()
        gb = int(gb)
        fl.append([gb, type])
fl.sort()
pA = []
pB = []
summ = 0
for fli in fl:
    if summ + fli[0] > s:
        break
    if fli[1] == "A":
        pA.append(fli)
    else:
        pB.append(fli)
    summ += fli[0]

kmax = len(pA) + len(pB)
print(len(pA))
for i in range(kmax, len(fl)):
    if fl[i][1] == "B":
        continue
    if summ - pB[-1][0] + fl[i][0] > s:
        break
    summ -= pB[-1][0]
    summ += fl[i][0]
    pA.append(fl[i])
    del pB[-1]
print(kmax)
print(len(pA))