alf = '346789'
c = "468"
n = "379"

def f(n):
    n = n - 1
    s = ""
    for i in range(6):
        s = alf[n%6] + s
        n//=6
    return s

for n in range(1, 6**6+1):
    s = f(n)
    kc = 0
    kn = 0
    for cif in s:
        if cif in c:
            kc += 1
        else:
            kn += 1

    if n % 2 == 1 and s[0] != "3" and kc > kn:
        print(n, s)
