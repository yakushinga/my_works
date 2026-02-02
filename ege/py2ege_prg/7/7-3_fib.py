"""
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан
следующими соотношениями:
  F(n) = 1 при n ≤ 2;
  F(n) = F(n − 1) + 2· F(n − 2) при n > 2.
Определите последние 6 цифр значения F(100).
"""

mem = {}
def F( n ):
  if n in mem: return mem[n]
  mem[n] = 1 if n <= 2 else \
           F(n-1) + 2*F(n-2)
  return mem[n]

print( F(100) % 10**6 )

#---------------------------

mem = [0]*101
def F( n ):
  if mem[n]: return mem[n]
  mem[n] = 1 if n <= 2 else \
           F(n-1) + 2*F(n-2)
  return mem[n]

print( F(100) % 10**6 )

#---------------------------

F = [0]*101
F[1] = F[2] = 1
for n in range(3,101):
  F[n] = 1 if n <= 2 else \
         F[n-1] + 2*F[n-2]
print( F[100] % 10**6 )

#---------------------------

from functools import cache
@cache
def F( n ):
  return 1 if n <= 2 else \
         F(n-1) + 2*F(n-2)
print( F(100) % 10**6 )

#---------------------------

def F( n ):
  if n <= 2: return 1
  fn1, fn2 = 1, 1
  for i in range(3,n+1):
    fn = fn1 + 2*fn2
    fn2 = fn1
    fn1 = fn
  return fn

print( F(100) % 10**6 )

#---------------------------

def F( n ):
  fn1, fn2 = 1, 1
  for i in range(3,n+1):
    fn1, fn2 = fn1 + 2*fn2, fn1
  return fn1

print( F(100) % 10**6 )


