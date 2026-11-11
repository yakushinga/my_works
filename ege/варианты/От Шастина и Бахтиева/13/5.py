def troi(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%3) + s
        n//=3
    return s

rmin = 900
for n in range(1, 1000):
    s = troi(n)
    if n % 3 == 0:
        s = "12" + s + "0"
    else:
        s = s + troi((n%3)*7)
    r = int(s, 3)
    if r >= 798 and r < rmin:
        rmin = r
print(rmin)