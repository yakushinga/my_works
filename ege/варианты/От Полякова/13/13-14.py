for x in range(10):
    n = 88000 + x*100 + 88 + 3 + x + 400 + 10000
    if n % 99 == 0:
        print(n//99)