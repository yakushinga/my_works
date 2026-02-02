"""
Для какого наименьшего целого неотрицательного A выражение
  (x· y < A) ∨ (x < y) ∨ (9 < x)
тождественно истинно, т. е. принимает значение 1 при любых целых
неотрицательных значениях переменных x и y?
(Ответ: 82)
"""
def f( x, y, A ):
  return (x*y < A) or (x < y) or (9 < x)

for A in range(1,1000):
  OK = True
  for x in range(1, 100):
    for y in range(1, 100):
      if not f(x, y, A):
        OK = False
        break
  if OK:
    print( A )
    break

for A in range(1,1000):
  if all( f(x, y, A) for x in range(1,100)
                     for y in range(1,100)):
    print( A )
    break

print( min( A for S in range(1,1000)
              if all( f(x, y, A) for x in range(1,100) for y in range(1,100) ) ) )