def f(n):
    a = []
    while n:
        a.append(n%125)
        n //= 125
    return a
a = f(17*125**453+117*5**231 - 3*5**13 - 2357)
n = 0
for k in a:
    if k <= 37:
        n += 1
print(n)