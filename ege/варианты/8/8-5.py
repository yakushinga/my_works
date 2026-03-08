def to(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%4) + s
        n//=4
    return s
def summcif(s):
    n = 0
    for i in range(len(s)):
        n += int(s[i])
    return n
rmin = 1000
for n in range(1000):
    s = to(n)
    k = summcif(s)
    if k%3 == 0:
        for i in range(len(s)):
            if s[i] == "0":
                s = s[:i] + "2" + s[i+1:]
            elif s[i] == "2":
                s = s[:i] + "0" + s[i+1:]
        s = "32" + s
    else:
        s = s[:1] + "10" + s[3:] + "33"
    r = int(s, 4)
    if r > 320 and r < rmin:
        rmin = r
        nmin = n
    elif r == rmin and n > nmin:
        nmin = n
print(nmin, to(r))