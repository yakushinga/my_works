"""
Среди чисел, больших, чем 10000000, найдите пять минимальных простых чисел.
(Ответ:
10000019
10000079
10000103
10000121
10000139)
"""
import timeit
def isPrime( n ):
  return all( n % d != 0
              for d in range(2,round(n**0.5)+1) )

t0 = timeit.default_timer()
count = 0
n = 10000000
while count < 5:
  if isPrime( n ):
    print( n )
    count += 1
  n += 1
print( timeit.default_timer() - t0 )


print('-----------------------------------------------')

t0 = timeit.default_timer()
count = 0
n = 10000000
results = []
while count < 5:
  if isPrime( n ):
    results.append( n )
    count += 1
  n += 1
print( *results )
print( timeit.default_timer() - t0 )

print('-----------------------------------------------')

t0 = timeit.default_timer()
count = 0
a, b = 10000000, 20000000
for n in range(a, b):
  if isPrime(n):
    print( n )
    count += 1
    if count >= 5: break

print( timeit.default_timer() - t0 )

print('-----------------------------------------------')

t0 = timeit.default_timer()
count = 0
a, b = 10000000, 20000000
results = []
for n in range(a, b):
  if isPrime(n):
    results.append( n )
    count += 1
    if count >= 5: break

print( *results )
print( timeit.default_timer() - t0 )

print('-----------------------------------------------')
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
n = 10000000
while count < 5:
  if len( divisors(n) ) == 2:
    print( n )
    count += 1
  n += 1
print( timeit.default_timer() - t0 )

print('-----------------------------------------------')

t0 = timeit.default_timer()
count = 0
a, b = 10000000, 20000000
for n in range(a, b):
  if len( divisors(n) ) == 2:
    print( n )
    count += 1
    if count >= 5: break

print( timeit.default_timer() - t0 )