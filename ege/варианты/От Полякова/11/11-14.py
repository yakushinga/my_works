def f(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%7) + s
        n//=7
    return s
for x in range(2031):
    if f(49**71+7**15-x).count("6") >= 11:
        print(x)