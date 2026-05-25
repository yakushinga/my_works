for n in range(1000000000):
    s = bin(n)[2:]
    r = int(str(bin(s.count("0"))[2:])+str(bin(s.count("1"))[2:]), 2)
    if r == 123:
        print(n)
        break