"""
Пусть S(N) – сумма трёх наибольших нетривиальных делителей числа N (не считая
единицы и самого числа). Если у числа N меньше трёх таких делителей, то S(N)
считается равным 0. Найдите 5 наибольших натуральных чисел, не превышающих
10 000 000, для которых S (N) – полный квадрат какого-либо числа. В ответе
запишите найденные числа в порядке возрастания, справа от каждого
числа запишите соответствующее ему значение S(N).
(Ответ:
)
"""
import timeit

def divisors( n ):
  q = round( n**0.5 )
  divs = []
  for d in range(1,q+1):
    if n % d == 0:
      divs.append( d )
      if n//d != d:
        divs.append( n//d )
  return sorted(divs)

def valid( n ):
  q = round(n**0.5)
  return n > 0 and q*q == n

t0 = timeit.default_timer()
n = 10_000_000
results = []
while len(results) < 5:
  divs = divisors( n )
  S = sum( divs[-4:-1] ) if len(divs) >= 5 else 0
  if valid( S ):
    print( S )
    results.append( S )
  n -= 1
print( *sorted(results) )
print( timeit.default_timer() - t0 )

print('---------------------------')

t0 = timeit.default_timer()
a, b = 0, 10_000_000
results = []
for n in range(b, a, -1):
  divs = divisors( n )
  S = sum( divs[-4:-1] ) if len(divs) >= 5 else 0
  if valid(S):
    results.append( S )
    if len(results) >= 5: break
  n -= 1
print( *sorted(results) )
print( timeit.default_timer() - t0 )