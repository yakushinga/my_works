def f(n):
    if n == 0:
        return "0"
    r = ""
    while n:
        r = str(n%3) + r
        n//=3
    return r
for n in range(3, 1000):
    s = f(n)
    if n%3 == 0:
        s = s + s[-2:]
    else:
        s = s + f(sum(list(map(int, s))))
    r = int(s, 3)
    if r > 220 and r%2 == 0:
        print(r)
        break