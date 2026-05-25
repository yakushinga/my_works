def to(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%4) + s
        n//=4
    return s
a = [1000, 1000]
for n in range(10000):
    s = to(n)
    print(s, sum(list(map(int, s))))
    if sum(list(map(int, s)))%4 == 0:
        for i in range(len(s)):
            if s == "3":
                s = s[:i] + "0" + s[i+1:]
            elif s == "0":
                s = s[:i] + "3" + s[i+1:]
        s = s + "21"
    else:
        s = "11" + s[2:] + "22"
    r = int(s, 4)
    if r > 200 and r < a[1]:
        a = [n, r]
    if r == a[1] and n < a[0]:
        a = [n, r]
print(a)
print(int("110101011",2))