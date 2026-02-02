"""
Пусть S(n) – сумма всех простых делителей натурального числа n. Найдите пять
наибольших натуральных чисел, не превышающих 300 000 000, у которых более
шести простых делителей. Программа должна вывести значения S(n) для найденных
чисел в порядке возрастания; справа от каждого значения S(n) нужно вывести
наибольший простой делитель числа n.
(Ответ:
78 37
216 73
222 89
310 181
501 433)
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

def isPrime( n ):
  return n > 1 and all( n % d != 0
              for d in range(2,round(n**0.5)+1) )

t0 = timeit.default_timer()
n = 300_000_000
results = []
count = 0
while count < 5:
  divs = divisors(n)
  primeDivs = [ d for d in divs if isPrime(d) ]
  if len(primeDivs) > 6:
    results.append( (sum(primeDivs), primeDivs[-1]) )
    count += 1
  n -= 1

for S, dMax in sorted(results):
  print( S, dMax )

print( timeit.default_timer() - t0 )

print('----------------------------------------')
t0 = timeit.default_timer()
n = 300_000_000
results = []
while len(results) < 5:
  divs = divisors(n)
  primeDivs = [ d for d in divs if isPrime(d) ]
  if len(primeDivs) > 6:
    results.append( (sum(primeDivs), primeDivs[-1]) )
  n -= 1

for S, dMax in sorted(results):
  print( S, dMax )

print( timeit.default_timer() - t0 )

print('----------------------------------------')
t0 = timeit.default_timer()
a, b = 0, 300_000_000
results, count = [], 0
for n in range(b, a, -1):
  divs = divisors(n)
  primeDivs = [ d for d in divs if isPrime(d) ]
  if len(primeDivs) > 6:
    results.append( (sum(primeDivs), primeDivs[-1]) )
    count += 1
    if count >= 5:
      break

for S, dMax in sorted(results):
  print( S, dMax )

print( timeit.default_timer() - t0 )

print('----------------------------------------')
t0 = timeit.default_timer()
a, b = 0, 300_000_000
results = []
for n in range(b, a, -1):
  divs = divisors(n)
  primeDivs = [ d for d in divs if isPrime(d) ]
  if len(primeDivs) > 6:
    results.append( (sum(primeDivs), primeDivs[-1]) )
    if len(results) >= 5:
      break

for S, dMax in sorted(results):
  print( S, dMax )

print( timeit.default_timer() - t0 )