k = 0
for n in range(1125000, 2000000):
    i = 2
    flag = False
    while i*i <= n:
        if n%i == 0:
            if i%10 == 7 and i != 7:
                flag = True
                d = i
                break
            if n//i%10 == 7 and n//i != 7:
                flag = True
                d = n//i
        i += 1
    if flag:
        print(n, d)
        k += 1
    if k == 5:
        break
