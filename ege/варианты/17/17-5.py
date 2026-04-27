for n in range(1, 1000000000):
    s = bin(n)[2:]
    k0 = s.count("0")
    k1 = s.count("1")
    s = bin(k0)[2:] + bin(k1)[2:]
    r = int(s, 2)
    if r == 214:
        print(n)
        break
print(bin(214)[2:])