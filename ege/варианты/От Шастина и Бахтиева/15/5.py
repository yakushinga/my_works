
for n in range(10000, 100000):
    a = list(map(int, str(n)))
    S1 = 0
    S2 = 0
    M = max(a) + min(a)
    for cif in a:
        if cif % 2 == 0:
            S1 += cif
        else:
            S2 += cif
    P1 = S1 + M
    P2 = S2 + M
    Pmax = max(P1, P2)
    Pmin = min(P1, P2)
    R = int(str(Pmin) + str(Pmax))
    if R == 812:
        print(n)