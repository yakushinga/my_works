"""
Составить функцию divisors, которая возвращает список всех делителей числа,
переданного её в качестве аргумента.
"""
def divisors( n ):
  divs = []
  for d in range(1, n+1):
    if n % d == 0:
      divs.append( d )
  return divs

print( divisors(28) )

def divisors( n ):
  q = round( n**0.5 )
  divs = []
  for d in range(1,q+1):
    if n % d == 0:
      divs.append( d )
      if n//d != d:
        divs.append( n//d )
  return sorted(divs)

def divisors( n ):
  q = round( n**0.5 )
  divs = set()
  for d in range(1,q+1):
    if n % d == 0:
      divs |= { d, n//d }
  return sorted(divs)

from time import time
start = time()
for n in range(1, 10**5):
  divisors( n )
print( time() - start )