def tr(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%3) + s
        n//=3
    return s
o = [0, 10000]
for n in range(1000):
    s = tr(n)
    if sum(list(map(int, s)))%3 == 0:
        for i in range(len(s)):
            if s[i] == "0":
                s = s[:i] + "1" + s[i+1:]
            elif s[i] == "1":
                s = s[:i] + "0" + s[i+1:]
        s = "10" + s
    else:
        s = "22" + s[2:] + "101"
    r = int(s, 3)
    if r > 314 and r < o[1]:
        o = [n, r]
    elif r == o[1] and n < o[0]:
        o = [n, r]
print(o)
print(16*26**6+18*26**5+15*26**4+4*26**3+21*26**2+3*26+20)