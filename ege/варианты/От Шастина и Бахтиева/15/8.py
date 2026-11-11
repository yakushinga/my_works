alf = "ОПАЧКИ"
gl = "ОАИ"
sgl = "ПЧК"
def f(n):
    s = ""
    for i in range(5):
        s = alf[n%6] + s
        n//=6
    return s

k = 0
for n in range(0, 6**5):
    s = f(n)
    flag = True
    for i in range(1, 5):
        if s[i] == s[i-1]:
            flag = False
            break
    if flag and not(s[0] in gl) and not(s[-1] in sgl):
        k += 1
        print(s)
print(k)