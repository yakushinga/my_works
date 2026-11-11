def f(n):
    if n % 2 == 0:
        return f(n//2) + 5
    if n % 5 == 0:
        return f(n//5) + 2
    return 0
m = [0]*1000001

m[1] = 0

for n in range(1, len(m)):
    if n%2 == 0:
        if n*2 <= len(m) - 1:
            m[n*2] += m[n] + 5
    else:
        if n*2 <= len(m) - 1:
            m[n*2] += m[n] + 5
        if n*5 <= len(m) - 1:
            m[n*5] += m[n] + 2
a = []
for i in m:
    if not i in a:
        a.append(i)
print(len(a))
