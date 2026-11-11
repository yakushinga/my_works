def f(n):
    k = 0
    while n:
        cif = n%16
        n//=16
        if cif > 9:
            k += 1
    return k
print(f(2*16**2020+9*16**2021-2*4**2022+8**2023-2*2**2024-65536))
