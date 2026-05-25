for n in range(1000):
    s = bin(n)[2:]
    summ = sum(map(int, s))
    if summ % 2 == 0:
        s = "10" + s[2:] + "0"
    else:
        s = "11" + s[2:] + "1"
    r = int(s, 2)
    if r > 480:
        print(n)
        break