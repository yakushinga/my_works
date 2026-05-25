alf = "АИКОТ"
def f(n):
    s = ''
    for i in range(5):
        s = alf[n%5] + s
        n//=5
    return s
for n in range(1, 5**5):
    s = f(n-1)
    if n%2 == 1 and not(s[0] in "КТ") and s.count("О") == 2:
        print(n, s)