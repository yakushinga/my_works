"""
Функция задана соотношениями
  F(n) = n при n ≤ 3;
  F(n) = F(n – 1) + 2 · F(n / 2)  при чётных n > 3;
  F(n) = F(n – 1) + F(n – 3)  при нечётных n > 3;
Определите, для скольких значений n из отрезка [1; 1000] значение функции
F(n) заканчивается на цифру 5.
"""
from functools import cache
@cache
def F( n ):
  return n if n <= 3 else \
         F(n-1) + F(n//2) if n % 2 == 0 else \
         F(n-1) - F(n-2)

N = 1000
count = 0
for n in range(1, N+1):
  if F(n) % 10 == 5:
    count += 1

print( count )

print('-------------------------------------')

N = 1000
F = [0]*(N+1)
F[1:4] = [1, 2, 3]
for n in range(4, N+1):
  F[n] = n if n <= 3 else \
         F[n-1] + F[n//2] if n % 2 == 0 else \
         F[n-1] - F[n-2]
count = 0
for n in range(1, N+1):
  if F[n] % 10 == 5:
    count += 1

print( count )

print('-------------------------------------')

N = 1000
F = [0]*(N+1)
F[1:4] = [1, 2, 3]
for n in range(4, N+1):
  F[n] = n if n <= 3 else \
         F[n-1] + F[n//2] if n % 2 == 0 else \
         F[n-1] - F[n-2]

elem5 = [ F[n] for n in range(4, N+1) if F[n] % 10 == 5 ]
print( len(elem5)  )

print( len( [ F[n] for n in range(4, N+1) if F[n] % 10 == 5 ] )  )

print( sum( F[n] % 10 == 5 for n in range(4, N+1) )  )

print('-------------------------------------')

N = 1000
F = [0]*(N+1)
F[1:4] = [1, 2, 3]
count = 0
for n in range(4, N+1):
  F[n] = n if n <= 3 else \
         F[n-1] + F[n//2] if n % 2 == 0 else \
         F[n-1] - F[n-2]
  if F[n] % 10 == 5:
    count += 1

print( count )

