def f(n):
    a = []
    while n:
        a = [n%27] + a
        n//=27
    return a.count(0)
for x in range(1, 27000):
    n = f(3*27**9+2*27**6+27**3-x)
    if n == 6:
        print(x)
        