def f(n):
    a = []
    while n:
        a.append(n%27)
        n//=27
    summ = 0
    for cif in a:
        if cif > 8 and cif%2 == 0:
            summ += cif
    return summ
print(f(7*729**2024+4*243**1413-6*81**169-2*9**107+4117))