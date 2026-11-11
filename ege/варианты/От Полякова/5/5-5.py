def pyat(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%5) + s
        n //= 5
    return s

def f(s):
    for i in range(len(s)):
        if s[i] == "1":
            s = s[:i] + "4" + s[i+1:]
        elif s[i] == "4":
            s = s[:i] + "1" + s[i+1:]
    s = "33" + s
    return s

for n in range(1, 2000):
    r = pyat(n)
    if r[-1] == "0":
        r = f(r)
    else:
        r = r + "44"
        r = "3" + r[1:len(r)-1] + "2"
    print(n, r, int(r,5))
