def tr(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%3) + s
        n//=3
    return s

def summ(s):
    m = list(map(int, s))
    return sum(m)

for n in range(9,1000):
    s = tr(n)
    if summ(s)%4 == 0:
        for i in range(len(s)):
            if s[i] == "1":
                s = s[:i] + "2" + s[i+1:]
            if s[i] == "2":
                s = s[:i] + "1" + s[i+1:]
        s = "10" + s
    else:
        s = s + "20"
        s = s[:1] + "02" + s[3:]
    if int(s, 3) > 302:
        print(n, int(s, 3), s)