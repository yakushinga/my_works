"""
Найдите все натуральные числа, принадлежащие отрезку [300_000_000; 500_000_000] и
имеющие ровно три нетривиальных делителя. Для каждого найденного числа выведите
само число и его наибольший нетривиальный делитель.
(Ответ:
352275361 2571353
373301041 2685619
492884401 3307949)
"""
def divisors( n ):
  root = round( n**0.5 )
  divs = []
  for d in range(1, root+1):
    if n % d == 0:
      divs.append( d )
      if n//d != d:
        divs.append( n//d )
  return sorted( divs )

def isPrime( n ):
  return all( n % d != 0
              for d in range(2,round(n**0.5)+1) )

"""
for n in range( 300_000_000, 500_000_000+1 ):
  divs = divisors( n )
  if len(divs) == 5:
    print( n, divs[-2] )
"""

from time import time
t0 = time()
from math import ceil
start = ceil(300_000_000**0.5)
end = int(500_000_000**0.5)
for root in range( start, end+1 ):
  divs = divisors( root*root )
  if len(divs) == 5:
    print( root*root, divs[-2] )
print( time() - t0 )

print('-----------------------------------')

t0 = time()
from math import ceil
start = ceil(300_000_000**0.25)
end = int(500_000_000**0.25)
for root4 in range( start, end+1 ):
  divs = divisors( root4**4 )
  if len(divs) == 5:
    print( root4**4, divs[-2] )
print( time() - t0 )


print('-----------------------------------')

import timeit
t0 = timeit.default_timer()

from math import ceil
start = ceil(300_000_000**0.25)
end = int(500_000_000**0.25)
for root4 in range( start, end+1 ):
  if isPrime(root4):
    print( root4**4, root4**3 )

print( timeit.default_timer() - t0 )
