alf = "".join(sorted("ОКУЛЬТИЗМ"))
from math import *
def f(n):
    n = n - 1
    s = ""
    for i in range(5):
        s = alf[n%9] + s
        n//=9
    return s

for n in range(1, 9**5+1):
    s = f(n)
    if n % 2 == 0 and s[0] in "ОУИ" and s.count("Ь") <= 1:
        print(n, s)
print(log(8192, 2))
print(bin(1667)[2:])
print(int("101111100111", 2))
print(bin(128)[2:])
print(bin(151)[2:])
