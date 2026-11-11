alf = "АЕЛПРЬ"
def f(n):
    n = n-1
    s = ""
    for i in range(5):
        s = alf[n%6]+s
        n//=6
    return s
for n in range(6**5):
    s = f(n)
    if n%2 == 0 and s[0] != "Ь" and s[0] != 'Р' and s.count("Л") >= 2:
        print(n)
print(f(7650))
print(bin(2047)[2:])