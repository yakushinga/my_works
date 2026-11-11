def f(n):
    a = []
    while n:
        a.append(n%121)
        n//=121
    k = 0
    for i in range(len(a)):
        if a[i] >= 64 and a[i] <= 104:
            k += 1
    return(k)
print(f(39*121**319 + 46*11**913 - 15*1331**15 - 1993 ))