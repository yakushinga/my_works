alf = "".join(sorted("ТОКСИЧНЫЙ"))

def f(s):
    k = 1
    n = 0
    for i in range(len(s)-1, -1, -1):
        n += alf.find(s[i])*k
        k*=len(alf)
    return n+5
print(f("ТОКСИЧНЫЙ"))