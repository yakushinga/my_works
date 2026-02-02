"""
Составить логическую функцию isPrime, которая возвращает логическое значение
True, если значение переданного ей аргумента – простое число, и False, если
это число составное.
"""
def isPrime( n ):
  for d in range(2,n):
    if n % d == 0:
      return False
  return True

p = []
for n in range(2, 100):
  if isPrime(n):
    p.append( n )
print( p )

#--------------------------------------------
def isPrime( n ):
  notDiv = [ n % d != 0 for d in range(2,n) ]
  return all( notDiv )

p = []
for n in range(2, 100):
  if isPrime(n):
    p.append( n )
print( p )

#--------------------------------------------
def isPrime( n ):
  return all( n % d != 0 for d in range(2,n) )

p = []
for n in range(2, 100):
  if isPrime(n):
    p.append( n )
print( p )

#--------------------------------------------
def isPrime( n ):
  q = round( n**0.5 )
  for d in range(2,q+1):
    if n % d == 0:
      return False
  return True

p = []
for n in range(2, 100):
  if isPrime(n):
    p.append( n )
print( p )

#--------------------------------------------
def isPrime( n ):
  return all( n % d != 0
              for d in range(2,round(n**0.5)+1) )

p = []
for n in range(2, 100):
  if isPrime(n):
    p.append( n )
print( p )