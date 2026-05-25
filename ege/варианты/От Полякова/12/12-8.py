alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def f(s):
    n = 0
    for i in range(len(s)-1, -1, -1):
        n += (alf.find(s[i])+1)*26**(len(s)-i-1)
    return n
print(f("SCREEN"))