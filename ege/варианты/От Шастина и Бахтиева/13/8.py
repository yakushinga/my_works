from math import *
def f(n):
    s = []
    for i in range(5):
        s = [n%15] + s
        n//=15
    return s
k = 0
for n in range(15**4, 15**5):
    flag = True
    a = f(n)
    if a.count(a[0]) != 1:
        flag = False
    for i in range(1, 5):
        if a[i] % 2 == a[i-1] % 2:
            flag = False
            break
        if a.count(a[i]) != 1:
            flag =  False
            break
    if a.count(5) + a.count(6) > 0:
        flag = False
    if flag:
        k += 1
print(k, log(512, 2))
