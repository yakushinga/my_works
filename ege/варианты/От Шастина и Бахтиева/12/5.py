for n in range(10000, 100000):
    c = list(map(int, str(n)))
    p1 = c[0]*c[2]
    p2 = c[2]*c[4]
    p3 = c[1] + c[3]
    p = [p1, p2, p3]
    p.sort()
    r = int(str(p[1]) + str(p[0]))
    if r == 3012:
        print(n)