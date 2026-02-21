with open ("17-428.txt") as f:
    c = f.read().split()
    for i in range(len(c)):
        c[i]=int(c[i])
k531 = 0
k773 = 0
for i in range(len(c)):
    if c[i]%531 == 0:
        k531 += 1
    if c[i]%773 == 0:
        k773 += 1
def summcif(n):
    n = abs(n)
    r = 0
    while n:
        r += n%10
        n //= 10
    return r
summtr = 0
k = 0
for i in range(len(c)-3):
    k1 = 0
    k2 = 0
    k3zn = 0
    for j in range(i, i+3):
        s = summcif(c[j])
        if s == k531:
            k1 += 1
        if s == k773:
            k2 += 1
        if abs(c[j]) >= 100 and abs(c[j]) < 1000:
            k3zn += 1
    if k1 <= 1 and k3zn > 0 and k2 >= 2:
        summtr += sum(c[i:i+3])
        k += 1
print(k, summtr/k)
