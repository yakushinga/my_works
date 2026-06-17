alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWX"

def f(s):
    k = 1
    n = 0
    for i in range(len(s)-1,-1,-1):
        n += alf.find(s[i])*k
        k*=34
    return n

for x in range (0, 34):
    ch = alf[x]
    n = f("5A24" + ch + "6H1") + f("7" + ch + "B83R7")
    if n % 33 == 0:
        print(n//33)