"""
Найдите все простые числа, принадлежащие числовому отрезку [33333; 55555],
сумма цифр которых больше 35. Запишите найденные числа в порядке возрастания,
справа от каждого – сумму его цифр.
(Ответ:
39799 37
39979 37
39989 38
48799 37
48889 37
48989 38
49789 37
49999 40)
"""
def isPrime( n ):
  return all( n % d != 0
              for d in range(2,round(n**0.5)+1) )

def sumDigits( n ):
  s = 0
  while n:
    s += n % 10
    n //= 10
  return s

def sumDigits( n ):
  return sum( map(int, str(n)) )

def sumDigits( n ):
  sn = str(n)
  s = 0
  for c in sn:
    s += int(c)
  return s

start, end = 33333, 55555
for n in range( start, end+1 ):
  if isPrime(n):
    s = sumDigits(n)
    if s > 35:
      print( n, s )

print('------------------------------')

for n in range( start, end+1 ):
  if isPrime(n) and sumDigits(n) > 35:
      print( n, sumDigits(n) )

print('------------------------------')

for n in range( start, end+1 ):
  if isPrime(n) and (s := sumDigits(n)) > 35:
      print( n, s )

print('------------------------------')

for n in range( start, end+1 ):
  isPrime = all( n % d != 0
                 for d in range(2,round(n**0.5)+1) )
  s = sum( map(int, str(n)) )
  if isPrime and s > 35:
      print( n, s )


