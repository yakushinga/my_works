with open ("17-418.txt") as f:
    c = list(map(int,f.read().split()))
def f(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%6) + s
        n//=6
    return len(s) == 4
def f1(n):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = str(n%9) + s
        n//=9
    return len(s) == 3
m1 = 1000000
m2 = 1000000
for n in c:
    if f(abs(n)):
        m1 = min(m1, n)
    if f1(abs(n)):
        m2 = min(m2, n)
o1 = abs(m1)%5
o2 = abs(m2)%13
a = []
for i in range(len(c)-3):
    k1 = 0
    k2 = 0
    for j in range(i, i+3):
        if abs(c[j])%11 == o1:
            k1 += 1
        if abs(c[j])%7 == o2:
            k2 += 1
    if k1 == 1 and k2 == 1:
        a.append(sum(c[i:i+3]))
print(len(a), min(a))