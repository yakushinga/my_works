N = 100000
F = [0]*N

for n in range(N):
    if n < 20:
        F[n] = n
    else:
        if n % 2 == 0:
            F[n] = F[n//2] + n - 7
        else:
            F[n] = F[n-4] + 8
maxF = 0

for el in F:
    if el >= 100 and el < 1000 and el > maxF:
        maxF = el

for i in range(N):
    if F[i] == maxF:
        print(i)