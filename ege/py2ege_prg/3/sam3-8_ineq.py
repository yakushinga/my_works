"""
Для какого наибольшего целого A найдутся такие целые неотрицательные x и y,
при которых выражение
(4· x + y > 115) ∨ (x > 3· y) ∨ (x + 4· y < A)
ложно?
(Ответ: 460)
"""

def f( x, y, A ):
  return (4*x + y > 115) or (x > 3*y) or (x + 4*y < A)

for A in range(600, 1, -1):
  OK = False
  for x in range(300):
    for y in range(300):
      if not f(x, y, A):
        OK = True
        break
    if OK: break
  if OK:
    print( A )
    break

print('----------------------------------')
for A in range(600,0,-1):
  if any( not f(x, y, A) for x in range(300)
                     for y in range(300)):
    print( A )
    break

print('----------------------------------')
print( max( A for A in range(1,600)
              if any( not f(x, y, A)
                for x in range(300) for y in range(300) ) ) )
