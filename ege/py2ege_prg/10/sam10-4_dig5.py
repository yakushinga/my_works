"""
В файле data10-4.txt в столбик записаны натуральные числа, не превышающие
10 000; их количество неизвестно.  Найдите максимальное из чисел, в десятичной
записи которых есть цифра 5. Гарантируется, что в файле есть хотя бы одно
число, в десятичной записи которого есть цифра 5.
(Ответ: 7537)
"""
def has5( n ):
  while n:
    if n % 10 == 5: return True
    n //= 10
  return False

def has5( n ):
  return any( d == '5' for d in str(n) )

max5 = 0
for s in open("data/data10-4.txt") :
  n = int( s )
  if has5( n ) and n > max5:
    max5 = n

print( max5 )

#----------------------------

data = [ int(s) for s in open("data/data10-4.txt") ]
data5 = [ n for n in data if has5( n ) ]
print( max(data5) )

#----------------------------

data5 = [ n for s in open("data/data10-4.txt")
           if has5( (n := int(s)) ) ]
print( max(data5) )

#----------------------------

print( max( n for s in open("data/data10-4.txt")
              if has5( (n := int(s)) ) ) )
