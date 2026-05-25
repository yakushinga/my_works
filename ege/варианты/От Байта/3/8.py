alf = "РПОГА"
def f(n):
    n = n - 1
    s = ""
    for i in range(5):
        s = alf[n%5] + s
        n //= 5
    return s
for n in range(1, 5**5):
    s = f(n)
    if s[0] != "Р" and s.count("Г") == 2 and s.count("ГГ") == 0 and s.count("О") == 0 and s.count("А") == 0:
        print(n, s)