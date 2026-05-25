def f(s):
    flag = 0
    k = 0
    for i in range(len(s)):
        if flag == 1 and int(s[i],12)%2 == 1:
            k += 1
        elif flag == 1 and int(s[i],12)%2 == 0:
            flag = 0
        elif flag == 0 and int(s[i],12)%2 == 1:
            flag = 1
    if k <= 2:
        return True
    return False
k = 0

def dven(n):
    a = "0123456789AB"
    s = ""
    while n:
        s = a[n%12] + s
        n //= 12
    return s

for n in range(12**4, 12**5):
    s = dven(n)
    if f(s):
        print(s)
        k += 1
print(k)