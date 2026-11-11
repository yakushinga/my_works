k = 0
for n in range(12**4, 12**5):
    k7 = 0
    k8 = 0
    while n:
        c = n%12
        if c == 7:
            k7 += 1
        if c > 8:
            k8 += 1
        n//=12
    if k7 == 1 and k8 <= 3:
        k += 1
print(k)
