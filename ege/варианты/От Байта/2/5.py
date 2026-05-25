for n in range(1, 100):
    s = bin(n)[2:]
    if n % 2 == 1:
        s = s + "1"
    else:
        s = s + "0"
    r = int(s, 2)
    if r >= 50:
        print(n)
        break