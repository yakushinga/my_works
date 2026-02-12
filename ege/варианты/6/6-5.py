def sem(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%7) + s
        n//=7
    return s

rmax = 0
for n in range (1, 2000):
    s = sem(n)
    if s[-1] == "2":
        for i in range(len(s)):
            if s[i] == "1":
                s = s[:i] + "3" + s[i+1:]
            elif s[i] == "3":
                s = s[:i] + "1" + s[i+1:]
        s  = "21" + s
    else:
        s = "1" + s[1:] + "36"
    r = int(s, 7)
    if r > rmax and r < 744:
        a = [n]
        rmax = r
    elif r == rmax:
        a.append(n)
print(a)