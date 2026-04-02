for n in range(100):
    s = bin(n)[2:]
    s = s + str(sum(map(int, s))%2)
    s = s + str(sum(map(int, s)) % 2)
    r = int(s, 2)
    if r > 85:
        print(n)
        break