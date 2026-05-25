def f(n):
    a = []
    while n:
        a.append(n%13)
        n//=13
    return a
for x in range(1, 5000):
    a = f(7*13**180+5*13**120-x)
    if a.count(0) == 60:
        print(x)