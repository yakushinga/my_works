alf = "0123456789AB"
def f(n):
    s = ""
    while n:
        s = alf[n%12] + s
        n//=12
    return s
minr = 10000
for n in range(1, 3000):
    s = f(n)
    if n % 4 == 0:
        s = "A" + s + "B"
    else:
        s = "1" + s + "0"
    r = int(s, 12)
    if r > 2025 and r < minr:
        minr = r
print(minr)
