for A in range(100):
    flag = True
    for x in range(100):
        for y in range(100):
            if not((3*x+y != 96) or (x <= y) or (A <= x)):
                flag = False
                break
        if not(flag):
            break
    if flag:
        print(A)