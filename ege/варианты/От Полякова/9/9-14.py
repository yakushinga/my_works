def f(n):
    a = []
    while n:
        a.append(n%49)
        n//=49
    k = 0
    for i in a:
        if i > 15:
            k += 1
    return k
print(f(15*49**237+37*343**500-14*7**35))