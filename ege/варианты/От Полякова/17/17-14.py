def f(n):
    s = ""
    while n:
        s = str(n%7) + s
        n//=7
    return s.count("0")
for x in range(1, 2300):
    if f(7**350 + 7**150 - x) == 200:
        print(x)