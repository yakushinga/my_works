for n in range(1000):
    s = bin(n)[2:]
    s = s + str(sum(list(map(int, s)))%2)
    s = s + str(sum(list(map(int, s))) % 2)
    r = int(s, 2)
    if r > 253:
        print(n)
        break
