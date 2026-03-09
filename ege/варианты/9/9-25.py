a = []
for n in range(-1, 10000):
    for m in range(-1, 10000):
        if n == -1:
            s1 = ""
        else:
            s1 = str(n)

        if m == -1:
            s2 = ""
        else:
            s2 = str(m)

        r = int("4" + s1 + "4736" + s2 + "1")
        if r <= 10**10 and r%7993 == 0:
            a.append(r)
a.sort()
for n in a:
    print(n, n//7993)
