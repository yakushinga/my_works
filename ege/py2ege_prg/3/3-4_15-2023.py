"""
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка
на натуральное число m». Для какого наименьшего натурального числа А формула
          (ДЕЛ(x, 2) → ¬ДЕЛ(x, 3)) or (x + A ≥ 100)
тождественно истинна (т.е. принимает значение 1) при любом натуральном
значении переменной х?
(Ответ: 94)
"""
def D( n, d ):
  return n % d == 0
def F( A ):
  for x in range(1, 1000):
    result = (D(x, 2) <= (not D(x, 3))) or (x + A >= 100)
    if not result:
      return False
  return True

A = 1
while not F( A ):
  A += 1

print( A )

#----------------------------------------------
def F( A ):
  xOK = [ (D(x, 2) <= (not D(x, 3))) or (x + A >= 100)
          for x in range(1, 1000) ]
  return all( xOK )
A = 1
while not F( A ):
  A += 1

print( A )

#----------------------------------------------
def F( A ):
  return all( (D(x, 2) <= (not D(x, 3))) or (x + A >= 100)
              for x in range(1, 1000) )
A = 1
while not F( A ):
  A += 1

print( A )

#----------------------------------------------
def F( A ):
  return all( ((x%2 == 0) <= (x%3!=0)) or (x + A >= 100)
              for x in range(1, 1000) )
A = 1
while not F( A ):
  A += 1

print( A )

#----------------------------------------------
A = 1
while not all( ((x%2 == 0) <= (x%3!=0)) or (x + A >= 100)
               for x in range(1, 1000) ):
  A += 1

print( A )

#----------------------------------------------
A = 1
while True:
  if all( ((x%2 == 0) <= (x%3!=0)) or (x + A >= 100)
          for x in range(1, 1000) ):
    break
  A += 1

print( A )


#----------------------------------------------
for A in range(1,1000):
  if F(A):
    print( A )
    break

#----------------------------------------------
for A in range(1,1000):
  if all( ((x%2 == 0) <= (x%3!=0)) or (x + A >= 100)
          for x in range(1, 1000) ):
    print( A )
    break



