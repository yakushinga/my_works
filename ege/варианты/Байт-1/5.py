for n in range(4, 1000):
    s = bin(n)[2:]
    if n % 4 == 0:
        s = s + s[:2]
    else:
        s = s + bin(n%4+1)[2:]
    r = int(s, 2)
    if r >= 50:
        print(n)
        break
print(int("111100", 2))