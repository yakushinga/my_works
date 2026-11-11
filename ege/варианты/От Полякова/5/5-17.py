with open("17-428.txt") as f:
    a = f.read().split('\n')
    del a[-1]
    for i in range(len(a)):
        a[i] = int(a[i])

d13 = []
d25 = []
for i in range(len(a)):
    if a[i]%13 == 0:
        d13.append(a[i])
    if a[i]%25 == 0:
        d25.append(a[i])

x = sum(map(int, str(d13[12])))
y = sum(map(int, str(d25[24])))

b = []
for i in range(len(a)-3):
    tr = 0
    ix = 0
    iy = 0
    for j in range (i, i+3):
        ix += sum(map(int,str(a[j]))) == x
        iy += sum(map(int, str(a[j]))) == y
        if a[j] >= 100 and a[j] <= 999:
            tr += 1
    if ix <= 1 and iy >= 2 and tr > 0:
        b.append(sum(a[i:i+3]))
print(len(b), int(sum(b)/len(b)))