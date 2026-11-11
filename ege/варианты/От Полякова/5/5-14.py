def f(n):
    a = []
    while n:
        a = [n%36] + a
        n //= 36
    return a

s = f(30*(36**231) + 18*(6**101) - 3*(36**45) - 2357 )
k = 0
print(s)
for i in range(len(s)):
    if (s[i]%3 == 0 or s[i]%5== 0) and s[i]%15 != 0:
        k+=1
        print(s[i])
print(k)