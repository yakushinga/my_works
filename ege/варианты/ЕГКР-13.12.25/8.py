alf = "АГИНРТ"
def f(n):
    s = ""
    n = n - 1
    for i in range(6):
        s = alf[n%6] + s
        n//=6
    return s
for n in range(1, 6**6):
    s = f(n)
    if n % 2 == 1 and not(s[0] in "АИГ") and s.count("А") == 1:
        print(n, s)
        break

print(bin(2028)[2:])
print(int("1111110110000", 2))