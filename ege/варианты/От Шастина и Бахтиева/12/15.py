for A in range(1000):
    flag = True
    for x in range(1000):
        if not(x&74 == 0 or (x&23 != 0 or x&A != 0)):
            flag = False
            break
    if flag:
        print(A)