alf = "АВНРЬЯ"
def f(n):
    s = ""
    for i in range(5):
        s = alf[n%6] + s
        n//=6
    return s

for n in range(1, 6**5+1):
    s = f(n-1)
    if s[0] != 'Я' and s.count("Ь") <= 1 and s.count("ЯЯ") == 0:
        print(n, s)