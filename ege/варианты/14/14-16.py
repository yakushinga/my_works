l = 10000000
m = [0]*l
for n in range(1, l//2+1):
    if n*2 < l:
        m[n*2] = m[n] + 5
    if n%2 == 1 and n*3 < l:
        m[n*3] = m[n] + 4
for n in range(l):
    if m[n] == 108:
        print(n)