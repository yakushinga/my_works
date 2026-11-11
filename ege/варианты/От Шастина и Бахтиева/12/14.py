alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def f(s, p):
    n = 0
    k = 1
    for i in range(len(s)-1, -1, -1):
        n += alf.find(s[i])*k
        k*=p
    return n

for p in range(16, 38):
    n = f("54367", p) + f("7F149", p) + f("B951C", p)
    if n % 13 == 0:
        print(p, n//13)