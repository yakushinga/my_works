"""
Пусть M(N) – произведение пять наименьших различных натуральных делителей
натурального числа N, не считая единицы. Если у числа N меньше пяти таких
делителей, то M(N) считается равным нулю. Найдите пять наименьших натуральных
чисел, превышающих 500 000 000, для которых 0 < M(N) < N. В ответе запишите
найденные значения M(N) в порядке возрастания соответствующих им чисел N.
(Ответ:
1152
24200
140608
720
5832)
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

t0 = timeit.default_timer()
count = 0
n = 500_000_001
while count < 5:
  divs = divisors(n)
  if len(divs) > 5:
    M = divs[1]*divs[2]*divs[3]*divs[4]*divs[5]
    if M < n:
      print( M )
      count += 1
  n += 1
print( timeit.default_timer() - t0 )

print('--------------------------------')

def divisors( n, limit = 0 ):
  q = round( n**0.5 )
  divs = []
  divCount = 0
  for d in range(1,q+1):
    if n % d == 0:
      divs.append( d )
      divCount += 1
      if n//d != d:
        divs.append( n//d )
      if limit and divCount >= limit:
        break
  return sorted(divs)

t0 = timeit.default_timer()
count = 0
n = 500_000_001
while count < 5:
  divs = divisors( n, 6 )
  if len(divs) > 5:
    M = divs[1]*divs[2]*divs[3]*divs[4]*divs[5]
    if M < n:
      print( M )
      count += 1
  n += 1
print( timeit.default_timer() - t0 )
