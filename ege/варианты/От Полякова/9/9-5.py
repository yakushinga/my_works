def to(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%5) + s
        n//=5
    return s

def summcif(s):
    return sum(list(map(int, list(s))))

rmin = 1000
nmin = 0
for n in range(1000):
    s = to(n)
    k = summcif(s)
    if k%5 == 0:
        for i in range(len(s)):
            if s[i] == "1":
                s = s[:i] + "0" + s[i+1:]
            elif s[i] == "0":
                s = s[:i] + "1" + s[i + 1:]
        s = s + "14"
    else:
        s = "44" + s[2:] + "33"
    r = int(s, 5)
    if r < rmin and r > 370:
        nmin = n
        rmin = r
    elif r == rmin and n < nmin:
        nmin = n
print(nmin, rmin)