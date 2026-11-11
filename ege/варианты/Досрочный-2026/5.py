for n in range(10000):
    s = bin(n)[2:]
    s = s + str(s.count("1")%2)
    s = s + str(s.count("1") % 2)
    r = int(s, 2)
    if r > 253:
        print(n, r, s)
        break