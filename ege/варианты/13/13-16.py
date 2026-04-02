l = 100000000
m = [0]*l
for n in range(1, l):
    if n*2 < l:
        m[n*2] += m[n] + 5
    if n*5 < l and n%2 == 1:
        m[n*5] += m[n] + 2
    if m[n] == 130:
        print(n)
