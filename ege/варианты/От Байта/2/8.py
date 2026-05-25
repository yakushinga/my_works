alf = "АКОТ"
def f(n):
    s = ""
    n = n - 1
    for i in range(5):
        s = alf[n%4] + s
        n//=4
    return s
for n in range(1, 4**5):
    s = f(n)
    flag90 = True
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            flag = False
    if s.count("А") == 2 and flag:
        print(n, s)