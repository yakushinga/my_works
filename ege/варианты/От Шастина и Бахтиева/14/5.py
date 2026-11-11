rmax = 0
for n in range(1, 1000):
    s = bin(n)[2:]
    sumcif = sum(map(int, s))
    if sumcif%2 == 0:
        s = "10" + s[2:] + "10"
    else:
        s = "11" + s[2:] + "01"
    r = int(s, 2)
    if r < 86 and r % 2 == 1 and r > rmax:
        rmax = r
print(rmax)